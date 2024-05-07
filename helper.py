import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(scores, mean_scores):
    plt.clf()  
    plt.title('Em treino...')
    plt.xlabel('Numero de Partidas')
    plt.ylabel('Pontuação')
    plt.plot(scores, label='Pontuação')
    plt.plot(mean_scores, label='Pontuação Média')
    plt.legend()  
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.pause(0.1)  
    display.display(plt.gcf())  
    display.clear_output(wait=True)  
