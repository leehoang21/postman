import 'package:flutter/material.dart';
import 'package:flutter_test_api/common/components/text_type.dart';

class StyleTextField extends StatefulWidget {
  // final List<TextInputFormatter>? formatNumber;
  final bool? autoFocus;
  final double width;
  final double height;
  final Function(String?)? selectItem;
  final List<String>? items;
  final String? value;
  final bool isDropdown;
  final bool? enabledCopyPaste;
  final bool enabled;
  final int? maxLine;
  final Color textColor;
  final StyleTextType textType;
  final String hintText;
  final Color titleColor;
  final Function(String)? onChanged;
  final bool isSecurity;
  final Widget? iconPrefix;
  final Widget? iconSuffix;
  final TextEditingController? controller;
  final TextInputAction inputAction;
  final FocusNode? focusNode;
  final Function()? onEditingComplete;
  final TextInputType? keyboardType;
  final Function()? onGetDate;
  final String? errorText;
  final double? borderRadius;
  final GlobalKey<FormState>? formKey;
  final Color borderColor;
  final String? Function(String?)? validator;
  final Color? backgroundColor;
  final FontStyle? fontStyle;
  const StyleTextField({
    Key? key,
    this.textColor = Colors.black,
    required this.hintText,
    this.titleColor = Colors.black,
    this.isSecurity = false,
    this.iconPrefix,
    this.iconSuffix,
    this.onChanged,
    this.controller,
    this.inputAction = TextInputAction.next,
    this.focusNode,
    this.onEditingComplete,
    this.keyboardType,
    this.onGetDate,
    this.errorText,
    this.enabled = true,
    this.isDropdown = false,
    this.selectItem,
    this.items,
    this.value,
    this.autoFocus = false,
    // this.formatNumber,
    this.height = 50,
    this.enabledCopyPaste = true,
    this.width = double.infinity,
    this.maxLine = 1,
    this.borderRadius,
    this.formKey,
    this.borderColor = Colors.transparent,
    this.validator,
    this.backgroundColor,
    this.fontStyle,
    this.textType = StyleTextType.paragraphRegular4,
  }) : super(key: key);

  @override
  State<StyleTextField> createState() => _StyleTextFieldState();
}

class _StyleTextFieldState extends State<StyleTextField> {
  bool _isObscure = false;
  @override
  Widget build(BuildContext context) {
    return Container(
      height: widget.height,
      width: widget.width,
      decoration: const BoxDecoration(),
      child: Form(
        key: widget.formKey,
        child: TextFormField(
          obscureText: _isObscure,
          validator: widget.validator,
          maxLines: widget.maxLine,
          enabled: widget.enabled,
          enableInteractiveSelection: widget.enabledCopyPaste!,
          onTap: widget.onGetDate,
          keyboardType: widget.keyboardType,
          textInputAction: widget.inputAction,
          autofocus: widget.autoFocus!,
          focusNode: widget.focusNode,
          onChanged: widget.onChanged,
          controller: widget.controller,
          style: TextStyle(
            backgroundColor: widget.backgroundColor,
            color: widget.textColor,
            fontWeight: widget.textType.weight,
            fontSize: widget.textType.size,
            fontStyle: widget.fontStyle,
          ),
          decoration: InputDecoration(
            enabled: widget.enabled,
            enabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(widget.borderRadius ?? 6),
              borderSide: BorderSide(
                  width: 1,
                  color: widget.borderColor), // change color you want...
            ),
            errorText: widget.errorText,
            contentPadding: EdgeInsets.only(
                top: 16,
                left: 16,
                right: widget.iconSuffix == null && widget.iconPrefix == null
                    ? 16
                    : 0),
            prefixIcon: widget.iconPrefix,
            suffixIcon: !widget.isSecurity
                ? widget.iconSuffix
                : IconButton(
                    icon: _isObscure
                        ? const Icon(
                            Icons.visibility_off_outlined,
                          )
                        : const Icon(
                            Icons.remove_red_eye,
                          ),
                    onPressed: () {
                      setState(
                        () {
                          _isObscure = !_isObscure;
                        },
                      );
                    },
                  ),
            border: OutlineInputBorder(
              borderSide: BorderSide(
                color: widget.borderColor,
              ),
              borderRadius: BorderRadius.circular(widget.borderRadius ?? 6),
            ),
            hintText: widget.hintText,
            hintStyle: TextStyle(
              color: widget.titleColor,
              fontWeight: widget.textType.weight,
              fontSize: widget.textType.size,
            ),
            focusedBorder: OutlineInputBorder(
              borderSide: BorderSide(color: widget.borderColor),
              borderRadius: BorderRadius.circular(widget.borderRadius ?? 6),
            ),
          ),
        ),
      ),
    );
  }
}

class StyleTextFieldProfileDropdown extends StatelessWidget {
  final String labelOutlineInput;
  final Function(String)? onChanged;
  final TextEditingController? controller;
  final bool isEnabled;
  final String? errorText;
  final TextInputType? textInputType;
  final String? time;
  final Function(String?)? selectItem;
  final List<String>? items;
  final String? text;
  final String? value;
  final FocusNode? focusNode;

  const StyleTextFieldProfileDropdown(
      {Key? key,
      required this.labelOutlineInput,
      this.onChanged,
      this.controller,
      this.isEnabled = true,
      this.errorText,
      this.textInputType = TextInputType.text,
      this.selectItem,
      this.items,
      this.time,
      this.text,
      this.value,
      this.focusNode})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return DropdownButtonFormField(
      focusNode: focusNode,
      value: value,
      decoration: InputDecoration(
        labelText: labelOutlineInput,
        errorText: errorText,
      ),
      items: items!.map((accountType) {
        return DropdownMenuItem(
          value: accountType,
          child: Text(accountType),
        );
      }).toList(),
      onChanged: selectItem,
    );
  }
}
