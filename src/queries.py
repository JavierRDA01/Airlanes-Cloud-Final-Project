import pyspark.sql.functions as F

def count_flights_by_airline(flightsDF):
    return (flightsDF
            .groupBy("Airline")
            .count()
            .orderBy(F.desc("count")))

def flight_event_summary_by_airline(flightsDF):
    return (flightsDF
            .groupBy("Airline")
            .agg(
                F.min("FlightDate").alias("first_flight_date"),
                F.max("FlightDate").alias("last_flight_date"),
                F.count("*").alias("total_flights")
            )
            .orderBy("Airline"))

# Nueva función agregada para corregir el error
def avg_arr_delay_by_day_of_week(flightsDF):
    return (flightsDF
            .groupBy("DayOfWeek")
            .agg(F.avg("ArrDelayMinutes").alias("avg_arr_delay"))
            .orderBy("DayOfWeek"))


def inverted_index_city_words_to_airlines(flightsDF):
    origin_words = (flightsDF
                    .select(F.col("Airline"), F.explode(F.split(F.col("OriginCityName"), " ")).alias("word")))

    dest_words = (flightsDF
                  .select(F.col("Airline"), F.explode(F.split(F.col("DestCityName"), " ")).alias("word")))

    all_words = origin_words.union(dest_words)

    result = (all_words
              .groupBy("word")
              .agg(F.collect_set("Airline").alias("airlines"))
              .orderBy("word"))

    # Convertir la columna airlines (ARRAY<STRING>) a STRING
    result = result.withColumn("airlines", F.concat_ws(",", F.col("airlines")))
    return result


def reverse_airport_link_graph(flightsDF):
    result = (flightsDF
              .select(F.col("Dest").alias("destination"), F.col("Origin").alias("source"))
              .groupBy("destination")
              .agg(F.collect_set("source").alias("sources"))
              .orderBy("destination"))
    
    # Convertir la columna sources (ARRAY<STRING>) a STRING
    result = result.withColumn("sources", F.concat_ws(",", F.col("sources")))
    return result

def filter_flights_with_high_arrival_delay(flightsDF):
    return flightsDF.filter(F.col("ArrDelayMinutes") > 30)

def distinct_routes(flightsDF):
    return flightsDF.select("Origin", "Dest").distinct()

def top_k_routes_by_arrival_delay(flightsDF, k):
    return (flightsDF
            .groupBy("Origin", "Dest")
            .agg(F.avg("ArrDelayMinutes").alias("avg_arr_delay"))
            .orderBy(F.desc("avg_arr_delay"))
            .limit(k))

def avg_dep_delay_by_airline(flightsDF):
    return (flightsDF
            .groupBy("Airline")
            .agg(F.avg("DepDelayMinutes").alias("avg_dep_delay"))
            .orderBy(F.desc("avg_dep_delay")))

def cancelled_ratio_by_airline(flightsDF):
    return (flightsDF
            .groupBy("Airline")
            .agg((F.sum(F.when(F.col("Cancelled") == 1, 1).otherwise(0))
                  / F.count("*")).alias("cancelled_ratio"))
            .orderBy(F.desc("cancelled_ratio")))

def avg_dep_delay_by_timeblock(flightsDF):
    return (flightsDF
            .groupBy("DepTimeBlk")
            .agg(F.avg("DepDelayMinutes").alias("avg_dep_delay"))
            .orderBy(F.desc("avg_dep_delay")))
