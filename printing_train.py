import time
import sys
from typing import Dict

def print_progress(current_epoch: int,
                  total_epochs: int,
                  current_batch: int,
                  total_batches: int,
                  metrics: Dict[str, float],
                  width: int = 30) -> None:
    """
    Imprime uma barra de progresso no estilo do Keras.
    
    Args:
        current_epoch: Época atual
        total_epochs: Número total de épocas
        current_batch: Batch atual
        total_batches: Número total de batches
        metrics: Dicionário com as métricas (nome: valor)
        width: Largura da barra de progresso
    """
    
    # Calcula a porcentagem completa
    progress = current_batch / total_batches
    
    # Cria a barra de progresso
    filled_width = int(width * progress)
    bar = '=' * filled_width + '>' + '.' * (width - filled_width - 1)
    
    # Formata o número do batch atual
    batch_display = str(current_batch).rjust(len(str(total_batches)))
    
    # Monta a string das métricas
    metrics_str = ' - '.join([f'{key}: {value:.4f}' for key, value in metrics.items()])
    print(metrics_str)
    # Monta a linha completa
    line = f'\rEpoch {current_epoch}/{total_epochs} - {batch_display}/{total_batches} [{bar}] - {metrics_str}'
    
    # Imprime a linha
    sys.stdout.write(line)
    sys.stdout.flush()
    
    # Adiciona uma nova linha se for o último batch
    if current_batch == total_batches:
        print()
