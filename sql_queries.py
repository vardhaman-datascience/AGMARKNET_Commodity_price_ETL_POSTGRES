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

create_markets = """
CREATE TABLE IF NOT EXISTS public.markets (
     market_id  SERIAL PRIMARY KEY,
     market_name VARCHAR
     
);
"""

drop_markets = "DROP TABLE IF EXISTS markets;"

markets_insert = """ INSERT INTO markets (market_name) VALUES ( %s) ON CONFLICT (market_id) DO NOTHING"""

create_state = """
CREATE TABLE IF NOT EXISTS public.state (
    stateid    SERIAL PRIMARY KEY,
    state_name  VARCHAR
   
);
"""

drop_state = "DROP TABLE IF EXISTS state;"

state_insert = """ INSERT INTO state (state_name) VALUES (%s) ON CONFLICT (stateid) DO NOTHING"""

create_district = """
CREATE TABLE IF NOT EXISTS district(
    districtid SERIAL PRIMARY KEY,
    district_name VARCHAR,
    state_name VARCHAR
    
);
"""

district_insert = """ INSERT INTO district (district_name,state_name) VALUES ( %s, %s) ON CONFLICT (districtid) DO NOTHING """

drop_district = "DROP TABLE IF EXISTS district;"

drop_table_queries = [drop_agmarknet, drop_markets, drop_state, drop_district]
create_table_queries = [create_agmarknet, create_markets, create_state, create_district]
