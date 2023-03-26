import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:flutter_test_api/presentation/journey/auth/cubit/forgot_pass_cubbit_cubit.dart';
import 'package:flutter_test_api/presentation/journey/auth/view/forgot_pass_screen.dart';

import '../../common/components/style_button.dart';

part 'app_routes.dart';

class AppPages {
  static String init = Routes.home;
  static Route<dynamic>? generateRoute(RouteSettings settings) {
    final argument = settings.arguments as Map<String, dynamic>?;
    switch (settings.name) {
      //home
      case Routes.home:
        return MaterialPageRoute(
          builder: (_) => BlocProvider(
            create: (context) => ForgotPassCubit(),
            child: const ForgotPassScreen(),
          ),
        );

      default:
        return _emptyRoute(settings);
    }
  }

  static MaterialPageRoute _emptyRoute(RouteSettings settings) {
    return MaterialPageRoute(
      builder: (context) => SizedBox(
        width: double.infinity,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ButtonWidget(
              onPressed: () {
                Navigator.pop(context);
              },
              title: 'No path for ${settings.name} Quay lại',
              width: 1.sw * 0.8,
              height: 1.sh * 0.05,
              titleColor: Colors.green,
              backgroundColor: Colors.red,
            ),
          ],
        ),
      ),
    );
  }
}
