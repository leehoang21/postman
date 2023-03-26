import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';

import '../../bloc/loading_bloc/loading_bloc.dart';
import '../../bloc/loading_bloc/loading_state.dart';
import 'loader_widget.dart';

class LoadingContainerWidget extends StatelessWidget {
  final Widget child;

  const LoadingContainerWidget({Key? key, required this.child})
      : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
        child,
        BlocBuilder<LoadingBloc, LoadingState>(
          builder: (context, state) {
            return Visibility(
              visible: state.status == LoadingStatus.loading,
              child: Center(
                child: Material(
                  elevation: 10,
                  borderRadius: BorderRadius.circular(10.r),
                  child: Container(
                    padding: const EdgeInsets.all(10),
                    width: 60,
                    height: 60,
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(10.r),
                      color: Colors.white,
                    ),
                    child: const LoaderWidget(),
                  ),
                ),
              ),
            );
          },
        )
      ],
    );
  }
}
