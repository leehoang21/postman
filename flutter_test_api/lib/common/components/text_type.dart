import 'dart:ui';

import 'package:flutter_screenutil/flutter_screenutil.dart';

enum StyleTextType {
  heading1,
  heading2,
  heading3,
  heading4,
  heading5,
  heading6,

  paragraphRegular0,
  paragraphRegular1,
  paragraphRegular2,
  paragraphRegular3,
  paragraphRegular3_5,
  paragraphRegular4,
  paragraphRegular5,

  paragraphBold1,
  paragraphBold2,
  paragraphBold3,
  paragraphBold4,

  medium22,
  medium18,
  medium16,
  medium15,
  medium14,

  w3h13,
}

extension StyleTextTypeExtension on StyleTextType {
  double get size {
    switch (this) {
      case StyleTextType.heading1:
        return 36.sp;
      case StyleTextType.heading2:
        return 24.sp;
      case StyleTextType.heading3:
        return 22.sp;
      case StyleTextType.heading4:
        return 18.sp;
      case StyleTextType.heading5:
        return 16.sp;
      case StyleTextType.heading6:
        return 14.sp;

      case StyleTextType.paragraphRegular0:
        return 20.sp;
      case StyleTextType.paragraphRegular1:
        return 18.sp;
      case StyleTextType.paragraphRegular2:
        return 16.sp;
      case StyleTextType.paragraphRegular3:
        return 14.sp;
      case StyleTextType.paragraphRegular3_5:
        return 13.sp;
      case StyleTextType.paragraphRegular4:
        return 12.sp;
      case StyleTextType.paragraphRegular5:
        return 10.sp;

      case StyleTextType.paragraphBold1:
        return 18.sp;
      case StyleTextType.paragraphBold2:
        return 16.sp;
      case StyleTextType.paragraphBold3:
        return 14.sp;
      case StyleTextType.paragraphBold4:
        return 12.sp;
      case StyleTextType.medium22:
        return 22.sp;
      case StyleTextType.medium18:
        return 18.sp;
      case StyleTextType.medium16:
        return 16.sp;
      case StyleTextType.medium15:
        return 15.sp;
      case StyleTextType.medium14:
        return 14.sp;
      case StyleTextType.w3h13:
        return 13.sp;
    }
  }

  FontWeight get weight {
    switch (this) {
      case StyleTextType.heading1:
      case StyleTextType.heading2:
      case StyleTextType.heading3:
      case StyleTextType.heading4:
      case StyleTextType.heading5:
      case StyleTextType.heading6:
        return FontWeight.w800;

      case StyleTextType.paragraphRegular0:
      case StyleTextType.paragraphRegular1:
      case StyleTextType.paragraphRegular2:
      case StyleTextType.paragraphRegular3:
      case StyleTextType.paragraphRegular3_5:
      case StyleTextType.paragraphRegular4:
      case StyleTextType.paragraphRegular5:
        return FontWeight.w400;

      case StyleTextType.paragraphBold1:
      case StyleTextType.paragraphBold2:
      case StyleTextType.paragraphBold3:
      case StyleTextType.paragraphBold4:
        return FontWeight.w600;

      case StyleTextType.medium22:
      case StyleTextType.medium18:
      case StyleTextType.medium16:
      case StyleTextType.medium15:
      case StyleTextType.medium14:
        return FontWeight.w500;
      case StyleTextType.w3h13:
        return FontWeight.w300;
    }
  }
}
