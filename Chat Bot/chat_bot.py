import aiml
import os


def chat():
    kernel = aiml.Kernel()
    kernel.verbose(0)
    kernel.setBotPredicate("name", "Mani")
    kernel.setPredicate('name', 'Sankar')

    if os.path.isfile("bot_brain.brn"):
        kernel.bootstrap(brainFile="bot_brain.brn")
    else:
        kernel.bootstrap(learnFiles="startup.xml", commands="LOAD AIML B")
        kernel.saveBrain("bot_brain.brn")

    print("Session Initiated. Type your message.")
    while True:
        excitation = input('')
        response = kernel.respond(excitation)
        if excitation == 'EXIT' or excitation == 'exit' or excitation == 'Exit':
            break
        else:
            print('>>> '+response)
            kernel.saveBrain("bot_brain.brn")
    print("Session Ended")


if __name__ == '__main__':
    chat()
