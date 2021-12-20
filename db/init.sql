-- Table: public.posts

-- DROP TABLE public.posts;

CREATE TABLE public.posts
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    title text COLLATE pg_catalog."C.UTF-8" NOT NULL,
    link text COLLATE pg_catalog."C.UTF-8" NOT NULL,
    description text COLLATE pg_catalog."C.UTF-8" NOT NULL,
    tags text COLLATE pg_catalog."C.UTF-8" NOT NULL,
    post_id integer NOT NULL,
    needs_to_post boolean,
    is_posted boolean NOT NULL DEFAULT false,
    CONSTRAINT posts_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

COMMENT ON COLUMN public.posts.post_id
    IS 'Habr post id';

COMMENT ON COLUMN public.posts.needs_to_post
    IS 'Needs to post this post on the Channel';

COMMENT ON COLUMN public.posts.is_posted
    IS 'Is posted on the channel';