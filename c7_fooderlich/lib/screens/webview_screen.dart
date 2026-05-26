import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

import '../models/models.dart';

class WebViewScreen extends StatefulWidget {
  static MaterialPage page() {
    return MaterialPage(
      name: FooderlichPages.raywenderlich,
      key: ValueKey(FooderlichPages.raywenderlich),
      child: const WebViewScreen(),
    );
  }

  const WebViewScreen({Key? key}) : super(key: key);

  @override
  WebViewScreenState createState() => WebViewScreenState();
}

class WebViewScreenState extends State<WebViewScreen> {
  late final WebViewController _controller;

  @override
  void initState() {
    super.initState();
    _controller = WebViewController()
      ..setJavaScriptMode(JavaScriptMode.unrestricted)
      ..loadRequest(Uri.parse('https://www.raywenderlich.com/'));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('raywenderlich.com'),
      ),
      body: WebViewWidget(controller: _controller),
    );
  }
}
