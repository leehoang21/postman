

import 'package:dio/dio.dart';

abstract class IApiService {
  Future<Response<T>> get<T>(String path, {Map<String, dynamic>? params});
  Future<Response<T>> post<T>(String path, {Map<String, dynamic>? params});
}
