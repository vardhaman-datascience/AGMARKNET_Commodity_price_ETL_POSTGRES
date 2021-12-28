create_agmarknet = """
CREATE TABLE IF NOT EXISTS public.agmarknet (
    state    VARCHAR ,
    district         VARCHAR,
    market           VARCHAR,
    commodity        VARCHAR,
    variety          VARCHAR,
    arrival_date     VARCHAR,
    min_price        FLOAT,
    max_price        FLOAT,
    modal_price      FLOAT
);
"""
     
drop_agmarknet = "DROP TABLE IF EXISTS agmarknet;"

agmarknet_insert = """
INSERT INTO agmarknet (state,district ,market , commodity ,variety, arrival_date  ,min_price    ,max_price  ,modal_price ) VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s) """

create_markets_lat_lng = """
CREATE TABLE IF NOT EXISTS public.market_lat_lng (
     market_name VARCHAR   PRIMARY KEY,
     lat FLOAT,
     lng FLOAT
     
);
"""

drop_market_lat_lng = "DROP TABLE IF EXISTS market_lat_lng;"

market_lat_lng_insert = """ INSERT INTO market_lat_lng (market_name,lat,lng) VALUES ( %s,%s,%s) ON CONFLICT (market_name) DO NOTHING"""

create_market_zipcode = """
CREATE TABLE IF NOT EXISTS public.market_zipcode (
    market_name    VARCHAR PRIMARY KEY,
    zipcode  INT
   
);
"""

drop_market_zipcode = "DROP TABLE IF EXISTS market_zipcode;"

market_zipcode_insert = """ INSERT INTO market_zipcode (market_name,zipcode) VALUES (%s,%s) ON CONFLICT (market_name) DO NOTHING"""



drop_table_queries = [drop_agmarknet, drop_market_lat_lng, drop_market_zipcode]
create_table_queries = [create_agmarknet, create_markets_lat_lng, create_market_zipcode]
