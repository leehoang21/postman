import 'package:flutter/widgets.dart';

class AuthClass {
  final GlobalKey<FormState> formKey = GlobalKey<FormState>();
  final String iconSvg;
  final TextEditingController controller = TextEditingController();
  final String? Function(String?) validator;
  final String label;

  AuthClass({
    required this.iconSvg,
    required this.validator,
    required this.label,
  });
}
