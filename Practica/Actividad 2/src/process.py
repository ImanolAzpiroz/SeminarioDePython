
def print_stats(stats):
    """
    Función que imprime la tabla de posiciones de los participantes
    
    Args:
        stats (dict): Un diccionario con los nombres de los participantes como claves y otro diccionario con sus estadísticas como valores.
        
    Returns:
        None
    """

    print("-" * 50)
    print("Tabla de posiciones: ")

    # Ordena por puntaje total de mayor a menor
    ranking = sorted(stats.items(), key=lambda x: x[1]['total_Score'], reverse=True)
    
    # print(ranking)
    # print(type(ranking))

    for i, (participant, participant_stats) in enumerate(ranking, start=1):
        print(f"{i}. {participant} - Rondas ganadas: {participant_stats['rounds_won']}, Puntaje total: {participant_stats['total_Score']}, Mejor puntaje: {participant_stats['best_score']}, Puntaje promedio: {participant_stats['average_Score']:.1f}")





def process(round, stats, round_number):
    """
    Función que procesa la información de una ronda y actualiza las estadísticas de los participantes.
    
    Args:
        round (dict): Un diccionario con el tema de la ronda(str) y las puntuaciones de los participantes(dict).
        stats (dict): Un diccionario con los nombres de los participantes como claves y otro diccionario con sus estadísticas como valores.
        round_number (int): El número de la ronda actual.
        
    Returns:
        None
    """

    # 'rounds_won' 'total_Score'  'best_score'  'average_Score' 
    winner = ' '
    max_score = -1


    for participant, scores in round['scores'].items():

        # puntaje total de la ronda
        round_total = sum(scores.values()) 

        if round_total > max_score:
            max_score = round_total
            winner = participant

        # total score
        stats[participant]['total_Score'] += round_total

        # best score
        if round_total > stats[participant]['best_score']:
            stats[participant]['best_score'] = round_total
        
        # average score (por ronda)
        stats[participant]['average_Score'] = stats[participant]['total_Score'] / round_number

    # rounds won
    stats[winner]['rounds_won'] += 1
    
    print(f'Ganador: {winner} con {max_score}pts.')

  


    