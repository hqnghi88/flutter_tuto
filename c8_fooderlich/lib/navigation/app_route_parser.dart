import 'package:flutter/material.dart';

import 'app_link.dart';

// 1
class AppRouteParser extends RouteInformationParser<AppLink> {
  // 2
  @override
  Future<AppLink> parseRouteInformation(
      RouteInformation routeInformation) async {
    // 3
    final link = AppLink.fromLocation(routeInformation.uri.toString());
    return link;
  }

  // 4
  @override
  RouteInformation restoreRouteInformation(AppLink configuration) {
    // 5
    final location = configuration.toLocation();
    // 6
    return RouteInformation(uri: Uri.parse(location));
  }
}
