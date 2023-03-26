import 'package:equatable/equatable.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

part 'forgot_pass_state.dart';

class ForgotPassCubit extends Cubit<FotgotPassState> {
  ForgotPassCubit() : super(FotgotPassCubbitInitial());
}
