import 'dart:ui';

import 'package:appflowy/core/helpers/helpers.dart';
import 'package:appflowy/startup/startup.dart';
import 'package:appflowy/startup/tasks/app_window_size_manager.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:window_manager/window_manager.dart';

class InitAppWindowTask extends LaunchTask with WindowListener {
  const InitAppWindowTask({
    this.minimumSize = const Size(800, 600),
    this.title = 'AppFlowy',
  });

  final Size minimumSize;
  final String title;

  @override
  Future<void> initialize(LaunchContext context) async {
    // Don't initialize on mobile or web.
    if (!defaultTargetPlatform.isDesktop || context.env.isIntegrationTest) {
      return;
    }

    await windowManager.ensureInitialized();
    windowManager.addListener(this);

    final windowSize = await WindowSizeManager().getSize();

    final windowOptions = WindowOptions(
      size: windowSize,
      minimumSize: const Size(
        WindowSizeManager.minWindowWidth,
        WindowSizeManager.minWindowHeight,
      ),
      title: title,
    );

    windowManager.waitUntilReadyToShow(windowOptions, () async {
      await windowManager.show();
      await windowManager.focus();

      final position = await WindowSizeManager().getPosition();
      if (position != null) {
        await windowManager.setPosition(position);
      }
    });
  }

  @override
  Future<void> onWindowResize() async {
    super.onWindowResize();

    final currentWindowSize = await windowManager.getSize();
    WindowSizeManager().setSize(currentWindowSize);
  }

  @override
  void onWindowMaximize() async {
    super.onWindowMaximize();

    final currentWindowSize = await windowManager.getSize();
    WindowSizeManager().setSize(currentWindowSize);
  }

  @override
  void onWindowMoved() async {
    super.onWindowMoved();

    final position = await windowManager.getPosition();
    WindowSizeManager().setPosition(position);
  }
}
