import argparse
import queries
from pyspark.sql import SparkSession

def main():
    # Configurar los argumentos de línea de comandos
    parser = argparse.ArgumentParser(description="Flight Analysis Application")
    parser.add_argument("--choice", type=int, required=True, help="Número de la consulta deseada")
    parser.add_argument("--k", type=int, help="Valor de K para la consulta 8 (opcional)")
    parser.add_argument("--input-path", type=str, required=True, help="Ruta del dataset de entrada")
    parser.add_argument("--output-path", type=str, required=True, help="Ruta de salida para guardar los resultados")
    args = parser.parse_args()

    # Crear sesión de Spark
    spark = (SparkSession.builder
             .appName("FlightAnalysisApp")
             .getOrCreate())

    # Leer el dataset desde la ruta proporcionada por el usuario
    try:
        flightsDF = spark.read.csv(args.input_path, header=True, inferSchema=True)
        print(f"Dataset cargado correctamente desde: {args.input_path}")
    except Exception as e:
        print(f"Error al cargar el dataset desde {args.input_path}: {e}")
        spark.stop()
        return

    # Ruta base para guardar resultados (proporcionada por el usuario)
    output_base_path = args.output_path

    # Ejecutar la consulta según la opción seleccionada
    if args.choice == 1:
        result = queries.count_flights_by_airline(flightsDF)
        output_path = f"{output_base_path}/consulta1_numero_vuelos_por_aerolinea"
    elif args.choice == 2:
        result = queries.flight_event_summary_by_airline(flightsDF)
        output_path = f"{output_base_path}/consulta2_eventos_por_aerolinea"
    elif args.choice == 3:
        result = queries.avg_arr_delay_by_day_of_week(flightsDF)
        output_path = f"{output_base_path}/consulta3_promedio_retraso_llegada"
    elif args.choice == 4:
        result = queries.inverted_index_city_words_to_airlines(flightsDF)
        output_path = f"{output_base_path}/consulta4_indice_invertido_ciudades_aerolineas"
    elif args.choice == 5:
        result = queries.reverse_airport_link_graph(flightsDF)
        output_path = f"{output_base_path}/consulta5_indice_invertido_aeropuertos"
    elif args.choice == 6:
        result = queries.filter_flights_with_high_arrival_delay(flightsDF)
        output_path = f"{output_base_path}/consulta6_vuelos_retraso_alto"
    elif args.choice == 7:
        result = queries.distinct_routes(flightsDF)
        output_path = f"{output_base_path}/consulta7_rutas_unicas"
    elif args.choice == 8:
        if not args.k:
            print("Debe proporcionar el valor de K para la consulta 8 con el argumento --k.")
            spark.stop()
            return
        result = queries.top_k_routes_by_arrival_delay(flightsDF, args.k)
        output_path = f"{output_base_path}/consulta8_top_k_rutas_retraso_promedio"
    elif args.choice == 9:
        result = queries.avg_dep_delay_by_airline(flightsDF)
        output_path = f"{output_base_path}/consulta9_promedio_retraso_salida"
    elif args.choice == 10:
        result = queries.cancelled_ratio_by_airline(flightsDF)
        output_path = f"{output_base_path}/consulta10_porcentaje_vuelos_cancelados"
    elif args.choice == 11:
        result = queries.avg_dep_delay_by_timeblock(flightsDF)
        output_path = f"{output_base_path}/consulta11_promedio_retraso_franja_horaria"
    else:
        print("Opción no válida.")
        spark.stop()
        return

    # Mostrar resultados y guardarlos
    result.show()
    try:
        result.write.mode("overwrite").csv(output_path)
        print(f"Resultados guardados en: {output_path}")
    except Exception as e:
        print(f"Error al guardar los resultados en {output_path}: {e}")
        spark.stop()
        return

    # Finalizar Spark
    spark.stop()

if __name__ == "__main__":
    main()
