import 'package:flutter/material.dart';

class StyleLabel extends StatelessWidget {
  final String title;
  final Color titleColor;
  final String? titleFontName;
  final FontStyle titleFontStyle;
  final FontWeight? titleFontWeight;
  final double? titleFontSize;
  final TextAlign textAlign;
  final int? maxLines;
  final TextDecoration? decoration;
  final FontStyle? fontStyle;
  final double? height;

  const StyleLabel(
      {Key? key,
      this.title = '',
      this.titleColor = Colors.black,
      this.titleFontName,
      this.titleFontStyle = FontStyle.normal,
      this.titleFontWeight,
      this.titleFontSize,
      this.textAlign = TextAlign.left,
      this.maxLines,
      this.decoration,
      this.fontStyle,
      this.height})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Text(
      title,
      textAlign: textAlign,
      maxLines: maxLines,
      overflow: TextOverflow.ellipsis,
      style: TextStyle(
        height: height,
        decoration: decoration,
        color: titleColor,
        fontStyle: fontStyle,
        fontSize: titleFontSize,
        fontFamily: titleFontName,
        fontWeight: titleFontWeight,
      ),
    );
  }
}
