import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutter_test_api/presentation/bloc/snackbar_bloc/snackbar_state.dart';

import 'snackbar_type.dart';

class SnackbarBloc extends Cubit<SnackbarState> {
  SnackbarBloc() : super(InitialSnackbarState());

  Future<void> showSnackbar(
      {required String translationKey,
      SnackBarType type = SnackBarType.error,
      List<dynamic>? params,
      Key? key}) async {
    emit(
      ShowSnackBarState(
        translationKey: translationKey,
        type: type,
        params: params ?? [],
        key: key,
      ),
    );
  }
}
