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
-- Name: books; Type: TABLE; Schema: librarians; Owner: postgres
--

CREATE TABLE books (
    id_b integer NOT NULL,
    title text NOT NULL,
    author text NOT NULL,
    count integer NOT NULL
);


ALTER TABLE books OWNER TO postgres;

--
-- Name: borrows; Type: TABLE; Schema: librarians; Owner: postgres
--

CREATE TABLE borrows (
    id_br integer NOT NULL,
    return date NOT NULL,
    rented date NOT NULL,
    name_id integer NOT NULL,
    book_id integer NOT NULL,
    give_back boolean
);


ALTER TABLE borrows OWNER TO postgres;

--
-- Name: readers; Type: TABLE; Schema: librarians; Owner: postgres
--

CREATE TABLE readers (
    id_r integer NOT NULL,
    name text NOT NULL,
    addres text NOT NULL
);


ALTER TABLE readers OWNER TO postgres;

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
-- Data for Name: books; Type: TABLE DATA; Schema: librarians; Owner: postgres
--

COPY books (id_b, title, author, count) FROM stdin;
0	null	null	30
5	Ferdydurke	Witold Gombrowicz	12
2	Dziady	Adam Mickiewicz	60
3	Lalka	Bolesław Prus	16
4	Wesele	Stanisław Wyspiański	4
1	Pan Tadeusz	Adam Mickiewicz	33
\.


--
-- Data for Name: borrows; Type: TABLE DATA; Schema: librarians; Owner: postgres
--

COPY borrows (id_br, return, rented, name_id, book_id, give_back) FROM stdin;
1	2017-03-25	2017-03-19	1	3	t
2	2017-03-30	2017-03-23	4	2	t
6	2017-04-27	2017-03-28	3	1	t
3	2017-03-23	2017-03-17	3	2	t
4	2017-03-19	2017-03-22	2	1	t
7	2017-05-01	2017-04-01	1	1	t
5	2017-03-14	2017-03-10	5	4	t
8	2017-05-01	2017-04-01	4	2	f
9	2017-05-01	2017-04-01	5	1	f
10	2017-05-01	2017-04-01	3	3	t
11	2017-05-02	2017-04-02	6	4	f
12	2017-05-02	2017-04-02	3	1	f
\.


--
-- Data for Name: readers; Type: TABLE DATA; Schema: librarians; Owner: postgres
--

COPY readers (id_r, name, addres) FROM stdin;
1	Jan Kowalski	Katowice, ul. Ogrodowa 2
2	Adam Kowalski	Katowice, ul. Ogrodowa 3
3	Janina Kowalska	Katowice, ul. Ogrodowa 2
4	Eryk Wincenty	Katowice, ul. Ogrodowa 10
5	Bogumiła Wypch	Katowice, ul. Ogrodowa 23
0	null	null
6	Adam Niedbalski	Katowice, Ogrdowa 126
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: librarians; Owner: postgres
--

COPY "user" (id, imie, nazwisko, email, haslo) FROM stdin;
1	Jakub	Jakub	hi@jakub.ovh	c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec
\.


--
-- Name: books books_pkey; Type: CONSTRAINT; Schema: librarians; Owner: postgres
--

ALTER TABLE ONLY books
    ADD CONSTRAINT books_pkey PRIMARY KEY (id_b);


--
-- Name: borrows borrows_pkey; Type: CONSTRAINT; Schema: librarians; Owner: postgres
--

ALTER TABLE ONLY borrows
    ADD CONSTRAINT borrows_pkey PRIMARY KEY (id_br);


--
-- Name: readers readers_pkey; Type: CONSTRAINT; Schema: librarians; Owner: postgres
--

ALTER TABLE ONLY readers
    ADD CONSTRAINT readers_pkey PRIMARY KEY (id_r);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: librarians; Owner: postgres
--

ALTER TABLE ONLY "user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: borrows book; Type: FK CONSTRAINT; Schema: librarians; Owner: postgres
--

ALTER TABLE ONLY borrows
    ADD CONSTRAINT book FOREIGN KEY (book_id) REFERENCES books(id_b);


--
-- Name: borrows reader; Type: FK CONSTRAINT; Schema: librarians; Owner: postgres
--

ALTER TABLE ONLY borrows
    ADD CONSTRAINT reader FOREIGN KEY (name_id) REFERENCES readers(id_r);


--
-- PostgreSQL database dump complete
--

