import logging

# --- Función auxiliar para validar enteros con logging ---
def input_int(prompt: str, min_val: int = None, max_val: int = None) -> int:
    """
    Solicita un entero al usuario, validando rango opcional.
    Registra advertencias en el log si la entrada es inválida
    """
    while True:
        try:
            valor = int(input(prompt).strip())
            if min_val is not None and valor < min_val:
                msg = f"Valor {valor} menor que mínimo {min_val}."
                print(msg)
                logging.warning(f"Entrada fuera de rango: {msg}")
                continue
            if max_val is not None and valor > max_val:
                msg = f"Valor {valor} mayor que máximo {max_val}."
                print(msg)
                logging.warning(f"Entrada fuera de rango: {msg}")
                continue
            return valor
        except ValueError:
            msg = "No ingresó un número entero válido."
            print(msg)
            logging.warning(f"Entrada inválida: {msg}")
