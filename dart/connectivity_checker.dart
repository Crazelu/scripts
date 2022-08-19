import "dart:io";

void main() async {
  final connected = await isUrlReachable(url: "google.com");
  print(connected);
}

Future<bool> isUrlReachable({
  required String url,
  Duration timeout = const Duration(seconds: 1),
}) async {
  try {
    if (!url.startsWith("http")) {
      url = "http://$url";
    }
    final client = HttpClient();
    client.connectionTimeout = timeout;
    await client.getUrl(Uri.parse(url));
    client.close(force: true);
    return true;
  } catch (e) {
    return false;
  }
}
