import matplotlib.pyplot as plt

def plot_scores(df, img):
    df.plot(kind='bar', x='home_team', y=['home_score', 'away_score'], stacked=True)
    plt.xlabel('Times')
    plt.ylabel('Gols')
    plt.title('Comparação de Gols')
    plt.savefig(img, format='png')