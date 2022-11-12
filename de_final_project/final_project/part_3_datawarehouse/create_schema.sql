-- This schema was pre-modelled using postgreSQL ERD tool in phpPgAdmin

BEGIN;

CREATE SCHEMA IF NOT EXISTS public
	AUTHORIZATION postgres;

CREATE TABLE IF NOT EXISTS public."softcartDimDate"
(
    year integer NOT NULL,
    dayofweek integer NOT NULL,
    month integer NOT NULL,
    monthname integer NOT NULL,
    day integer NOT NULL,
    dateid integer NOT NULL,
    date date NOT NULL,
    quarter integer NOT NULL,
    quartername character varying NOT NULL,
    PRIMARY KEY (dateid)
);

CREATE TABLE IF NOT EXISTS public."softcartDimCategory"
(
    categoryid integer NOT NULL,
    category character varying NOT NULL,
    PRIMARY KEY (categoryid)
);

CREATE TABLE IF NOT EXISTS public."softcartDimCountry"
(
    countryid integer NOT NULL,
    country character varying NOT NULL,
    PRIMARY KEY (countryid)
);

CREATE TABLE IF NOT EXISTS public."softcartDimItem"
(
    itemid integer NOT NULL,
    item character varying NOT NULL,
    PRIMARY KEY (itemid)
);

CREATE TABLE IF NOT EXISTS public."softcartFactSales"
(
    dateid integer NOT NULL REFERENCES public."softcartDimDate" (dateid),
    orderid integer NOT NULL,
    categoryid integer NOT NULL REFERENCES public."softcartDimCategory" (categoryid),
    itemid integer NOT NULL REFERENCES public."softcartDimItem" (itemid),
    countryid integer NOT NULL NOT NULL REFERENCES public."softcartDimCountry" (countryid),
    price numeric NOT NULL,
    PRIMARY KEY (orderid)
);


END;