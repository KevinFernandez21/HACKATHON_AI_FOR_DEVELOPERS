import 'package:flutter/material.dart';

class QuizAnswers {
  static List<String> selectedAnswers = [];

  static void saveAnswer(String answer) {
    selectedAnswers.add(answer);
  }
}

class QuizTemplate extends StatefulWidget {
  final String question;
  final List<String> options;
  final Function(String) onNext;
  final Color backgroundColor;
  final Color buttonColor;
  final Function() onNextScreen;

  const QuizTemplate({
    super.key,
    required this.question,
    required this.options,
    required this.onNext,
    required this.backgroundColor,
    required this.buttonColor,
    required this.onNextScreen,
  });

  @override
  QuizTemplateState createState() => QuizTemplateState();
}

class QuizTemplateState extends State<QuizTemplate> {
  String? selectedOption;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: widget.backgroundColor,
      body: Center(
        child: Container(
          padding: const EdgeInsets.all(20.0),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(12),
            boxShadow: [
              BoxShadow(
                color: Colors.grey.withOpacity(0.5),
                spreadRadius: 5,
                blurRadius: 7,
                offset: const Offset(0, 3),
              ),
            ],
          ),
          width: 300,
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: <Widget>[
              const Text(
                'Tiempo Social',
                textAlign: TextAlign.center,
                style: TextStyle(
                  fontSize: 24.0,
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 20.0),
              Text(
                widget.question,
                textAlign: TextAlign.center,
              ),
              const SizedBox(height: 20.0),
              for (var option in widget.options)
                Padding(
                  padding: const EdgeInsets.symmetric(vertical: 4.0),
                  child: ElevatedButton(
                    onPressed: () {
                      setState(() {
                        selectedOption = option;
                      });
                    },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: selectedOption == option
                          ? widget.buttonColor
                          : Colors.white,
                      foregroundColor: selectedOption == option
                          ? Colors.white
                          : Colors.black,
                      side: BorderSide(
                        color: selectedOption == option
                            ? widget.buttonColor
                            : Colors.grey,
                      ),
                    ),
                    child: Text(option),
                  ),
                ),
              const SizedBox(height: 20.0),
              Align(
                alignment: Alignment.centerRight,
                child: ElevatedButton(
                  onPressed: () {
                    if (selectedOption != null) {
                      widget.onNext(selectedOption!);
                      widget.onNextScreen();
                    } else {
                      ScaffoldMessenger.of(context).showSnackBar(
                        const SnackBar(
                            content: Text('Por favor selecciona una opción antes de continuar')),
                      );
                    }
                  },
                  style: ElevatedButton.styleFrom(
                    backgroundColor: widget.buttonColor,
                    foregroundColor: Colors.white,
                    padding: const EdgeInsets.symmetric(
                      horizontal: 24.0,
                      vertical: 12.0,
                    ),
                  ),
                  child: const Text('Siguiente'),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class QuizScreen1 extends StatelessWidget {
  const QuizScreen1({super.key});

  @override
  Widget build(BuildContext context) {
    return QuizTemplate(
      question: 'Dispongo de suficiente tiempo para dedicarlo a mi familia, amigos, pasatiempos y ocio.',
      options: const ['Casi nunca', 'A veces', 'Casi siempre'],
      onNext: (String answer) {
        QuizAnswers.saveAnswer(answer);
      },
      backgroundColor: Colors.pink[50]!,
      buttonColor: Colors.pink,
      onNextScreen: () {
        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => const QuizScreen2()),
        );
      },
    );
  }
}

class QuizScreen2 extends StatelessWidget {
  const QuizScreen2({super.key});

  @override
  Widget build(BuildContext context) {
    return QuizTemplate(
      question: 'Dispongo de suficiente tiempo para dedicarlo a mi familia, amigos, pasatiempos y ocio.',
      options: const ['Casi nunca', 'A veces', 'Casi siempre'],
      onNext: (String answer) {
        QuizAnswers.saveAnswer(answer);
      },
      backgroundColor: Colors.blue[50]!,
      buttonColor: Colors.pink,
      onNextScreen: () {
        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => const QuizScreen3()),
        );
      },
    );
  }
}

class QuizScreen3 extends StatelessWidget {
  const QuizScreen3({super.key});

  @override
  Widget build(BuildContext context) {
    return QuizTemplate(
      question: 'Dispongo de suficiente tiempo para dedicarlo a mi familia, amigos, pasatiempos y ocio.',
      options: const ['Casi nunca', 'A veces', 'Casi siempre'],
      onNext: (String answer) {
        QuizAnswers.saveAnswer(answer);
      },
      backgroundColor: Colors.blue[50]!,
      buttonColor: Colors.pink,
      onNextScreen: () {
        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => const QuizScreen4()),
        );
      },
    );
  }
}

class QuizScreen4 extends StatelessWidget {
  const QuizScreen4({super.key});

  @override
  Widget build(BuildContext context) {
    return QuizTemplate(
      question: 'Dispongo de suficiente tiempo para dedicarlo a mi familia, amigos, pasatiempos y ocio.',
      options: const ['Casi nunca', 'A veces', 'Casi siempre'],
      onNext: (String answer) {
        QuizAnswers.saveAnswer(answer);
      },
      backgroundColor: Colors.blue[50]!,
      buttonColor: Colors.pink,
      onNextScreen: () {
        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => const ResultScreen()),
        );
      },
    );
  }
}

class ResultScreen extends StatelessWidget {
  const ResultScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Resultados'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: ListView.builder(
          itemCount: QuizAnswers.selectedAnswers.length,
          itemBuilder: (context, index) {
            return ListTile(
              leading: CircleAvatar(
                child: Text('${index + 1}'),
              ),
              title: Text('Pregunta ${index + 1}:'),
              subtitle: Text('Respuesta: ${QuizAnswers.selectedAnswers[index]}'),
            );
          },
        ),
      ),
    );
  }
}
