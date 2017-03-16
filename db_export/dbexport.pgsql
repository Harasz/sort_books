--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.2
-- Dumped by pg_dump version 9.6.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: librarians; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA librarians;


ALTER SCHEMA librarians OWNER TO postgres;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = librarians, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: librarians; Owner: postgres
--

CREATE TABLE "user" (
    id integer NOT NULL,
    imie text NOT NULL,
    nazwisko text NOT NULL,
    email text NOT NULL,
    haslo text NOT NULL
);


ALTER TABLE "user" OWNER TO postgres;

--
-- Data for Name: user; Type: TABLE DATA; Schema: librarians; Owner: postgres
--

COPY "user" (id, imie, nazwisko, email, haslo) FROM stdin;
1	Jakub	Jakub	hi@jakub.ovh	c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: librarians; Owner: postgres
--

ALTER TABLE ONLY "user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

