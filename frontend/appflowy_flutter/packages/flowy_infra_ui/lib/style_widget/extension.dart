import 'package:flutter/material.dart';
export 'package:styled_widget/styled_widget.dart';

extension FlowyStyledWidget on Widget {
  Widget bottomBorder({double width = 1.0, Color color = Colors.grey}) {
    return DecoratedBox(
      decoration: BoxDecoration(
        border: Border(
          bottom: BorderSide(width: width, color: color),
        ),
      ),
      child: this,
    );
  }

  Widget topBorder({double width = 1.0, Color color = Colors.grey}) {
    return DecoratedBox(
      decoration: BoxDecoration(
        border: Border(
          top: BorderSide(width: width, color: color),
        ),
      ),
      child: this,
    );
  }
}

class TopBorder extends StatelessWidget {
  const TopBorder({
    super.key,
    this.width = 1.0,
    this.color = Colors.grey,
    required this.child,
  });

  final Widget child;
  final double width;
  final Color color;

  @override
  Widget build(BuildContext context) {
    return DecoratedBox(
      decoration: BoxDecoration(
        border: Border(
          top: BorderSide(width: width, color: color),
        ),
      ),
      child: child,
    );
  }
}
