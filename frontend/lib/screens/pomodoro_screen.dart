import 'dart:async';
import 'package:flutter/material.dart';

int hexToInteger(String hex) => int.parse(hex, radix: 16);

class AttendanceScreen extends StatefulWidget {
  AttendanceScreen();

  @override
  _AttendanceScreenState createState() => _AttendanceScreenState();
}

class _AttendanceScreenState extends State<AttendanceScreen> {
  static var countdownDuration = Duration(minutes: 10);
  Duration duration = Duration();
  Timer? timer;
  bool countDown = true;

  @override
  void initState() {
    var mints;
    var secs;
    mints = int.parse("25");
    secs = int.parse("00");
    countdownDuration = Duration(minutes: mints, seconds: secs);
    startTimer();
    reset();

    super.initState();
  }

  void startTimer() {
    timer = Timer.periodic(Duration(seconds: 1), (_) => addTime());
  }

  void reset() {
    if (countDown) {
      setState(() => duration = countdownDuration);
    } else {
      setState(() => duration = Duration());
    }
  }

  void addTime() {
    final addSeconds = 1;
    setState(() {
      final seconds = duration.inSeconds - addSeconds;
      if (seconds < 0) {
        timer?.cancel();
      } else {
        duration = Duration(seconds: seconds);
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      child: buildTime(),
    );
  }

  Widget buildTime() {
    String twoDigits(int n) => n.toString().padLeft(2, '0');
    final minutes = twoDigits(duration.inMinutes.remainder(60));
    final seconds = twoDigits(duration.inSeconds.remainder(60));

    return WillPopScope(
      onWillPop: _onWillPop,
      child: Container(
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Container(
              child: Text(
                '$minutes : $seconds',
                style: TextStyle(
                  color: Color(0xFFFF8DB6),
                  fontWeight: FontWeight.bold,
                  fontSize: 24.0,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Future<bool> _onWillPop() async {
    final isRunning = timer == null ? false : timer!.isActive;
    if (isRunning) {
      timer!.cancel();
    }
    Navigator.of(context, rootNavigator: true).pop(context);
    return true;
  }
}

class MyAppBar extends StatelessWidget {
  const MyAppBar({required this.title, super.key});

  // Fields in a Widget subclass are always marked "final".

  final Widget title;

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 56, // in logical pixels
      padding: const EdgeInsets.symmetric(horizontal: 8),
      decoration: BoxDecoration(color: Colors.blue[500]),
      // Row is a horizontal, linear layout.
      child: Row(
        children: [
          const IconButton(
            icon: Icon(Icons.menu),
            tooltip: 'Navigation menu',
            onPressed: null, // null disables the button
          ),
          // Expanded expands its child
          // to fill the available space.
          Expanded(
            child: title,
          ),
          const IconButton(
            icon: Icon(Icons.search),
            tooltip: 'Search',
            onPressed: null,
          ),
        ],
      ),
    );
  }
}

class MyScaffold extends StatelessWidget {
  const MyScaffold({super.key});

  @override
  Widget build(BuildContext context) {
    // Material is a conceptual piece
    // of paper on which the UI appears.
    return Material(
      // Column is a vertical, linear layout.
      child: Column(
        children: [
          Expanded(
            child: Center(
              child: AttendanceScreen(),
            ),
          ),
        ],
      ),
    );
  }
}

void main() {
  runApp(
    MaterialApp(
      title: 'My app', // used by the OS task switcher
      theme: ThemeData(
        colorScheme: ColorScheme(
          primary: Color(0xFFB93C5D),
          onPrimary: Colors.black,
          secondary: Color(0xFFEFF3F3),
          onSecondary: Color(0xFF322942),
          error: Colors.redAccent,
          onError: Colors.white,
          background: Color(0xFFFFFF),
          onBackground: Color(0xFFFFFF),
          surface: Color(0xFFFFFF),
          onSurface: Color(0xFF241E30),
          brightness: Brightness.light,
        ),
      ),
      home: SafeArea(
        child: MyScaffold(),
      ),
    ),
  );
}