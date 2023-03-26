import 'package:flutter/material.dart';
import 'package:flutter_test_api/common/components/text_type.dart';

import '../contant/layout_contant.dart';
import 'style_label.dart';

class ButtonWidget extends StatelessWidget {
  const ButtonWidget({
    Key? key,
    this.title = '',
    this.titleColor = Colors.black,
    this.titleFontStyle = FontStyle.normal,
    this.textType = StyleTextType.paragraphRegular4,
    this.width,
    this.height,
    this.borderRadius,
    required this.onPressed,
    this.backgroundColor = Colors.transparent,
    this.leading,
    this.trailing,
  }) : super(key: key);
  final String title;
  final Color titleColor;
  final FontStyle titleFontStyle;
  final StyleTextType textType;
  final double? width;
  final double? height;
  final double? borderRadius;
  final VoidCallback onPressed;
  final Color backgroundColor;
  final Widget? leading;
  final Widget? trailing;
  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: width,
      height: height,
      child: TextButton(
        onPressed: onPressed,
        style: ButtonStyle(
          backgroundColor: MaterialStateProperty.all<Color>(backgroundColor),
          shape: MaterialStateProperty.all<RoundedRectangleBorder>(
            RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(
                borderRadius ?? LayoutConstants.buttonRadius,
              ),
            ),
          ),
        ),
        child: Row(
          children: [
            leading ?? const SizedBox(),
            Center(
              child: StyleLabel(
                title: title,
                titleColor: titleColor,
                titleFontStyle: titleFontStyle,
                titleFontSize: textType.size,
                titleFontWeight: textType.weight,
              ),
            ),
            trailing ?? const SizedBox(),
          ],
        ),
      ),
    );
  }
}
