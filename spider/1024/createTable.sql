drop table if exists ONLINE_LINKs;
create table ONLINE_LINKS(
    TITLE varchar(100),
    URL varchar(100),
    POST_DATE date,
    REPLY_COUNT int,
    STATUS int
);
delete from online_links;
select * from online_links;
select count(1) from online_links;
select * from online_links where status = 0;

select * from online_links where url like '%4441128%';
