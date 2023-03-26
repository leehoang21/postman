import 'package:dio/dio.dart';
import 'package:flutter_test_api/common/api_service/api_service.dart';

class ApiServiceImpl extends IApiService {
  final Dio dio;
  final int requestTimeOut = 30;

  ApiServiceImpl({
    required this.dio,
  }) {
    dio.options.baseUrl = '';
    dio.options.connectTimeout = Duration(seconds: requestTimeOut);
    dio.options.receiveTimeout = Duration(seconds: requestTimeOut);
  }

  @override
  Future<Response<T>> get<T>(String path, {Map<String, dynamic>? params}) {
    return dio.get<T>(
      path,
      queryParameters: params,
    );
  }

  @override
  Future<Response<T>> post<T>(String path, {Map<String, dynamic>? params}) {
    final FormData? formData;
    if (params != null) {
      formData = FormData.fromMap(params);
    } else {
      formData = null;
    }
    return dio.post<T>(
      path,
      data: formData,
    );
  }
}
