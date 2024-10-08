import 'dart:convert';

import 'package:appflowy/core/config/kv.dart';
import 'package:appflowy/core/config/kv_keys.dart';
import 'package:appflowy/startup/startup.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:freezed_annotation/freezed_annotation.dart';
part 'folder_bloc.freezed.dart';

enum FolderCategoryType {
  favorite,
  personal,
}

class FolderBloc extends Bloc<FolderEvent, FolderState> {
  FolderBloc({
    required FolderCategoryType type,
  }) : super(FolderState.initial(type)) {
    on<FolderEvent>((event, emit) async {
      await event.map(
        initial: (e) async {
          // fetch the expand status
          final isExpanded = await _getFolderExpandStatus();
          emit(state.copyWith(isExpanded: isExpanded));
        },
        expandOrUnExpand: (e) async {
          final isExpanded = e.isExpanded ?? !state.isExpanded;
          await _setFolderExpandStatus(e.isExpanded ?? !state.isExpanded);
          emit(state.copyWith(isExpanded: isExpanded));
        },
      );
    });
  }

  Future<void> _setFolderExpandStatus(bool isExpanded) async {
    final result = await getIt<KeyValueStorage>().get(KVKeys.expandedViews);
    final map = result.fold(
      (l) => {},
      (r) => jsonDecode(r),
    );
    if (isExpanded) {
      // set expand status to true if it's not expanded
      map[state.type.name] = true;
    } else {
      // remove the expand status if it's expanded
      map.remove(state.type.name);
    }
    await getIt<KeyValueStorage>().set(KVKeys.expandedViews, jsonEncode(map));
  }

  Future<bool> _getFolderExpandStatus() async {
    return getIt<KeyValueStorage>().get(KVKeys.expandedViews).then((result) {
      return result.fold((l) => true, (r) {
        final map = jsonDecode(r);
        return map[state.type.name] ?? true;
      });
    });
  }
}

@freezed
class FolderEvent with _$FolderEvent {
  const factory FolderEvent.initial() = Initial;
  const factory FolderEvent.expandOrUnExpand({
    bool? isExpanded,
  }) = ExpandOrUnExpand;
}

@freezed
class FolderState with _$FolderState {
  const factory FolderState({
    required FolderCategoryType type,
    required bool isExpanded,
  }) = _FolderState;

  factory FolderState.initial(
    FolderCategoryType type,
  ) =>
      FolderState(
        type: type,
        isExpanded: true,
      );
}
