import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';

import '../../common/contant/layout_contant.dart';
import '../bloc/loading_bloc/loading_bloc.dart';
import '../bloc/snackbar_bloc/snackbar_bloc.dart';
import '../bloc/snackbar_bloc/snackbar_state.dart';
import '../bloc/snackbar_bloc/snackbar_type.dart';
import '../routes/app_pages.dart';
import '../widget/loading_widget/loading_container_widget.dart';
import '../widget/snackbar_widget/snackbar_widget.dart';

class App extends StatelessWidget {
  const App({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final GlobalKey<NavigatorState> navigatorKey = GlobalKey<NavigatorState>();
    return ScreenUtilInit(
      designSize: const Size(
        LayoutConstants.widthDefault,
        LayoutConstants.heightDefault,
      ),
      builder: (BuildContext context, Widget? child) {
        return MultiBlocProvider(
          providers: [
            BlocProvider(
              create: (context) => SnackbarBloc(),
            ),
            BlocProvider(
              create: (context) => LoadingBloc(),
            ),
          ],
          child: SafeArea(
            child: MaterialApp(
              navigatorKey: navigatorKey,
              debugShowCheckedModeBanner: false,
              onGenerateRoute: AppPages.generateRoute,
              initialRoute: AppPages.init,
              builder: (context, widget) {
                return LoadingContainerWidget(
                  child: _buildBlocListener(widget, context, navigatorKey),
                );
              },
            ),
          ),
        );
      },
    );
  }

  BlocListener<SnackbarBloc, SnackbarState> _buildBlocListener(
    Widget? widget,
    BuildContext context,
    GlobalKey<NavigatorState> navigatorKey,
  ) {
    return BlocListener<SnackbarBloc, SnackbarState>(
      listener: (context, state) {
        if (state is ShowSnackBarState) {
          TopSnackBar(
            title: state.translationKey ?? '',
            type: state.type ?? SnackBarType.error,
            key: state.key,
          ).showWithNavigator(
            navigatorKey.currentState ?? NavigatorState(),
            context,
          );
        }
      },
      child: widget,
    );
  }
}
