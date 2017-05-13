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
-- Name: books_id_b_seq; Type: SEQUENCE; Schema: librarians; Owner: postgres
--

CREATE SEQUENCE books_id_b_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE books_id_b_seq OWNER TO postgres;

--
-- Name: books_id_b_seq; Type: SEQUENCE OWNED BY; Schema: librarians; Owner: postgres
--

ALTER SEQUENCE books_id_b_seq OWNED BY books.id_b;


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
-- Name: borrows_id_br_seq; Type: SEQUENCE; Schema: librarians; Owner: postgres
--

CREATE SEQUENCE borrows_id_br_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE borrows_id_br_seq OWNER TO postgres;

--
-- Name: borrows_id_br_seq; Type: SEQUENCE OWNED BY; Schema: librarians; Owner: postgres
--

ALTER SEQUENCE borrows_id_br_seq OWNED BY borrows.id_br;


--
-- Name: comments; Type: TABLE; Schema: librarians; Owner: postgres
--

CREATE TABLE comments (
    id_comment integer NOT NULL,
    id_b integer NOT NULL,
    comment text NOT NULL,
    date date NOT NULL,
    r_name text NOT NULL,
    accept boolean
);


ALTER TABLE comments OWNER TO postgres;

--
-- Name: comments_id_comment_seq; Type: SEQUENCE; Schema: librarians; Owner: postgres
--

CREATE SEQUENCE comments_id_comment_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE comments_id_comment_seq OWNER TO postgres;

--
-- Name: comments_id_comment_seq; Type: SEQUENCE OWNED BY; Schema: librarians; Owner: postgres
--

ALTER SEQUENCE comments_id_comment_seq OWNED BY comments.id_comment;


--
-- Name: readers; Type: TABLE; Schema: librarians; Owner: postgres
--

CREATE TABLE readers (
    id_r integer NOT NULL,
    name text NOT NULL,
    addres text NOT NULL,
    email text,
    pass text NOT NULL,
    loged boolean NOT NULL,
    login text NOT NULL
);


ALTER TABLE readers OWNER TO postgres;

--
-- Name: readers_id_r_seq; Type: SEQUENCE; Schema: librarians; Owner: postgres
--

CREATE SEQUENCE readers_id_r_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE readers_id_r_seq OWNER TO postgres;

--
-- Name: readers_id_r_seq; Type: SEQUENCE OWNED BY; Schema: librarians; Owner: postgres
--

ALTER SEQUENCE readers_id_r_seq OWNED BY readers.id_r;


--
-- Name: readers_pref; Type: TABLE; Schema: librarians; Owner: postgres
--

CREATE TABLE readers_pref (
    reader_id integer NOT NULL,
    allow_email boolean NOT NULL,
    allow_address boolean NOT NULL,
    allow_profile boolean NOT NULL
);


ALTER TABLE readers_pref OWNER TO postgres;

--
-- Name: user; Type: TABLE; Schema: librarians; Owner: postgres
--

CREATE TABLE "user" (
    id integer NOT NULL,
    imie text NOT NULL,
    nazwisko text NOT NULL,
    email text NOT NULL,
    haslo text NOT NULL,
    master boolean
);


ALTER TABLE "user" OWNER TO postgres;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: librarians; Owner: postgres
--

CREATE SEQUENCE user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE user_id_seq OWNER TO postgres;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: librarians; Owner: postgres
--

ALTER SEQUENCE user_id_seq OWNED BY "user".id;


--
-- Name: books id_b; Type: DEFAULT; Schema: librarians; Owner: postgres
--

ALTER TABLE ONLY books ALTER COLUMN id_b SET DEFAULT nextval('books_id_b_seq'::regclass);


--
-- Name: borrows id_br; Type: DEFAULT; Schema: librarians; Owner: postgres
--

ALTER TABLE ONLY borrows ALTER COLUMN id_br SET DEFAULT nextval('borrows_id_br_seq'::regclass);


--
-- Name: comments id_comment; Type: DEFAULT; Schema: librarians; Owner: postgres
--

ALTER TABLE ONLY comments ALTER COLUMN id_comment SET DEFAULT nextval('comments_id_comment_seq'::regclass);


--
-- Name: readers id_r; Type: DEFAULT; Schema: librarians; Owner: postgres
--

ALTER TABLE ONLY readers ALTER COLUMN id_r SET DEFAULT nextval('readers_id_r_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: librarians; Owner: postgres
--

ALTER TABLE ONLY "user" ALTER COLUMN id SET DEFAULT nextval('user_id_seq'::regclass);


--
-- Data for Name: books; Type: TABLE DATA; Schema: librarians; Owner: postgres
--

COPY books (id_b, title, author, count) FROM stdin;
3	Lalka	Bolesław Prus	16
5	Ferdydurke	Witold Gombrowicz	12
2	Dziady	Adam Mickiewicz	40
7	Harry Potter i Kamień Filozoficzny	J.K. Rowling	15
1	Pan Tadeusz	Adam Mickiewicz	35
4	Wesele	Stanisław Wyspiański	3
\.


--
-- Name: books_id_b_seq; Type: SEQUENCE SET; Schema: librarians; Owner: postgres
--

SELECT pg_catalog.setval('books_id_b_seq', 8, true);


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
15	2017-05-13	2017-04-13	4	4	f
16	2017-05-13	2017-04-13	2	4	f
17	2017-05-13	2017-04-13	1	5	t
14	2017-04-17	2017-04-13	1	4	t
18	2017-04-17	2017-04-13	1	5	t
20	2017-04-18	2017-04-18	2	1	t
21	2017-04-18	2017-04-18	1	1	t
11	2017-05-02	2017-04-02	6	4	t
12	2017-05-02	2017-04-02	3	1	t
22	2017-05-04	2017-05-04	9	7	t
13	2017-05-09	2017-04-13	3	4	t
\.


--
-- Name: borrows_id_br_seq; Type: SEQUENCE SET; Schema: librarians; Owner: postgres
--

SELECT pg_catalog.setval('borrows_id_br_seq', 22, true);


--
-- Data for Name: comments; Type: TABLE DATA; Schema: librarians; Owner: postgres
--

COPY comments (id_comment, id_b, comment, date, r_name, accept) FROM stdin;
0	2	polecam każdemu <3	2017-04-20	Eryk Wincenty	\N
1	1	Super książka polecam!	2017-05-03	Jan Kowalski	t
\.


--
-- Name: comments_id_comment_seq; Type: SEQUENCE SET; Schema: librarians; Owner: postgres
--

SELECT pg_catalog.setval('comments_id_comment_seq', 1, true);


--
-- Data for Name: readers; Type: TABLE DATA; Schema: librarians; Owner: postgres
--

COPY readers (id_r, name, addres, email, pass, loged, login) FROM stdin;
4	Eryk Wincenty	Katowice, ul. Ogrodowa 10	test@test.pl	3c9909afec25354d551dae21590bb26e38d53f2173b8d3dc3eee4c047e7ab1c1eb8b85103e3be7ba613b31bb5c9c36214dc9f14a42fd7a2fdb84856bca5c44c2	t	test4
2	Adam Kowalski	Katowice, ul. Ogrodowa 3	test@test.pl	3c9909afec25354d551dae21590bb26e38d53f2173b8d3dc3eee4c047e7ab1c1eb8b85103e3be7ba613b31bb5c9c36214dc9f14a42fd7a2fdb84856bca5c44c2	t	test2
1	Jan Kowalski	Katowice, ul. Ogrodowa 2	jan@jan.pl	3c9909afec25354d551dae21590bb26e38d53f2173b8d3dc3eee4c047e7ab1c1eb8b85103e3be7ba613b31bb5c9c36214dc9f14a42fd7a2fdb84856bca5c44c2	t	test1
3	Janina Kowalska	Katowice, ul. Ogrodowa 2	asd@ads.pl	d404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176b6db28512f2e000b9d04fba5133e8b1c6e8df59db3a8ab9d60be4b97cc9e81db	t	test3
6	Adam Niedbalski	Katowice, Ogrdowa 126	brak	3c9909afec25354d551dae21590bb26e38d53f2173b8d3dc3eee4c047e7ab1c1eb8b85103e3be7ba613b31bb5c9c36214dc9f14a42fd7a2fdb84856bca5c44c2	f	test6
5	Bogumiła Wypch	Katowice, ul. Ogrodowa 20	test@test.pl	3c9909afec25354d551dae21590bb26e38d53f2173b8d3dc3eee4c047e7ab1c1eb8b85103e3be7ba613b31bb5c9c36214dc9f14a42fd7a2fdb84856bca5c44c2	t	test5
8	Jakub Kiepka	Gliwice, ul. Ogrodowa 2	null	c7ac587b56b7e33f681fedb8bab3bb1a41b5fe744e39a3f6705dab83bf37a118287c57862f54c826dc149eabdb7857cd5cc6d6171be2254b4d8b45aee5180f8c	f	JaKie692
9	Olek Olewski	Gliwice, ul. Gliwicka 22	Olek@gmail.com	3c9909afec25354d551dae21590bb26e38d53f2173b8d3dc3eee4c047e7ab1c1eb8b85103e3be7ba613b31bb5c9c36214dc9f14a42fd7a2fdb84856bca5c44c2	t	OlOle735
\.


--
-- Name: readers_id_r_seq; Type: SEQUENCE SET; Schema: librarians; Owner: postgres
--

SELECT pg_catalog.setval('readers_id_r_seq', 9, true);


--
-- Data for Name: readers_pref; Type: TABLE DATA; Schema: librarians; Owner: postgres
--

COPY readers_pref (reader_id, allow_email, allow_address, allow_profile) FROM stdin;
2	f	f	f
3	f	t	f
4	f	f	f
5	t	f	t
1	f	t	t
9	t	f	t
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: librarians; Owner: postgres
--

COPY "user" (id, imie, nazwisko, email, haslo, master) FROM stdin;
0	Jakub	Sydor	hi@jakub.ovh	c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec	t
3	Grażyna	Kowal	grazyna@kowal.pl	343adb962355c1fc1453d4e24ed16380aa08500a2797f659aeeb71b8484649256c8d62de68eb57da856dca444e60abbf8adbd1d74df185fbd57452f666452e2c	f
\.


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: librarians; Owner: postgres
--

SELECT pg_catalog.setval('user_id_seq', 4, true);


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
-- Name: comments comments_pkey; Type: CONSTRAINT; Schema: librarians; Owner: postgres
--

ALTER TABLE ONLY comments
    ADD CONSTRAINT comments_pkey PRIMARY KEY (id_comment);


--
-- Name: readers readers_pkey; Type: CONSTRAINT; Schema: librarians; Owner: postgres
--

ALTER TABLE ONLY readers
    ADD CONSTRAINT readers_pkey PRIMARY KEY (id_r);


--
-- Name: readers_pref readers_pref_pkey; Type: CONSTRAINT; Schema: librarians; Owner: postgres
--

ALTER TABLE ONLY readers_pref
    ADD CONSTRAINT readers_pref_pkey PRIMARY KEY (reader_id);


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

