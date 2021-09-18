--
-- PostgreSQL database dump
--

-- Dumped from database version 13.4
-- Dumped by pg_dump version 13.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

-- SET default_table_access_method = heap;

--
-- Name: epathshala_quiz_responses1; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.epathshala_quiz_responses1 (
    id integer NOT NULL,
    deviceid character varying(255),
    phoneno character varying(255),
    udise character varying(255),
    stuname character varying(255),
    grade integer,
    quizno integer NOT NULL,
    subject character varying(255),
    quizstatus character varying(255),
    q1 integer,
    q2 integer,
    q3 integer,
    q4 integer,
    q5 integer,
    q6 integer,
    q7 integer,
    q8 integer,
    q9 integer,
    q10 integer,
    totmarks integer,
    maxmarks integer,
    instance_id character varying NOT NULL,
    created_at timestamp without time zone DEFAULT now(),
    start_time timestamp with time zone,
    end_time timestamp with time zone,
    today character varying(10)
);


--ALTER TABLE public.epathshala_quiz_responses1 OWNER TO postgres;

--
-- Name: epathshala_quiz_responses1_normalized_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.epathshala_quiz_responses1_normalized_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--ALTER TABLE public.epathshala_quiz_responses1_normalized_id_seq OWNER TO postgres;

--
-- Name: epathshala_quiz_responses1_normalized_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.epathshala_quiz_responses1_normalized_id_seq OWNED BY public.epathshala_quiz_responses1.id;


--
-- Name: prerna_saathi_final; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.prerna_saathi_final (
    whatsapp_number character varying(15) NOT NULL,
    volunteer_name character varying(255),
    gender character varying(30),
    age character varying(45),
    phone_number character varying(15),
    school_udise_code character varying(30),
    student_opted_number integer,
    student_1_name character varying(255),
    student_1_grade real,
    student_1_number character varying(15),
    student_2_name character varying(255),
    student_2_grade real,
    student_2_number character varying(15),
    student_3_name character varying(255),
    student_3_grade real,
    student_3_number character varying(15),
    student_4_name character varying(255),
    student_4_grade real,
    student_4_number character varying(15),
    student_5_name character varying(255),
    student_5_grade real,
    student_5_number character varying(15),
    student_6_name character varying(255),
    student_6_grade real,
    student_6_number character varying(15),
    student_7_name character varying(255),
    student_7_grade real,
    student_7_number character varying(15),
    student_8_name character varying(255),
    student_8_grade real,
    student_8_number character varying(15),
    student_9_name character varying(255),
    student_9_grade real,
    student_9_number character varying(15),
    student_10_name character varying(255),
    student_10_grade real,
    student_10_number character varying(15),
    device_id character varying(100),
    registration_date date,
    instance_id character varying(255),
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    deleted_at timestamp without time zone
);


--ALTER TABLE public.prerna_saathi_final OWNER TO postgres;

--
-- Name: prerna_saathi_final_normalized; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.prerna_saathi_final_normalized (
    id integer NOT NULL,
    school_udise_code character varying(30),
    student_name character varying(255),
    student_grade integer,
    student_number character varying(15),
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    deleted_at timestamp without time zone
);


--ALTER TABLE public.prerna_saathi_final_normalized OWNER TO postgres;

--
-- Name: prerna_saathi_final_normalized_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.prerna_saathi_final_normalized_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--ALTER TABLE public.prerna_saathi_final_normalized_id_seq OWNER TO postgres;

--
-- Name: prerna_saathi_final_normalized_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.prerna_saathi_final_normalized_id_seq OWNED BY public.prerna_saathi_final_normalized.id;


--
-- Name: epathshala_quiz_responses1 id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.epathshala_quiz_responses1 ALTER COLUMN id SET DEFAULT nextval('public.epathshala_quiz_responses1_normalized_id_seq'::regclass);


--
-- Name: prerna_saathi_final_normalized id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prerna_saathi_final_normalized ALTER COLUMN id SET DEFAULT nextval('public.prerna_saathi_final_normalized_id_seq'::regclass);


--
-- Name: epathshala_quiz_responses1 epathshala_quiz_responses1_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.epathshala_quiz_responses1
    ADD CONSTRAINT epathshala_quiz_responses1_pkey PRIMARY KEY (id);


--
-- Name: prerna_saathi_final_normalized prerna_saathi_final_normalized_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prerna_saathi_final_normalized
    ADD CONSTRAINT prerna_saathi_final_normalized_pkey PRIMARY KEY (id);


--
-- Name: prerna_saathi_final prerna_saathi_final_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prerna_saathi_final
    ADD CONSTRAINT prerna_saathi_final_pkey PRIMARY KEY (whatsapp_number);


--
-- Name: unique_instance_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX unique_instance_id ON public.epathshala_quiz_responses1 USING btree (instance_id);


--
-- PostgreSQL database dump complete
--

