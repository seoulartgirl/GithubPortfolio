use testdb2;

-- 학생 stdent, 학과 department 테이블을 생성하고 각각 3개씩 데이터를 입력
-- 기본키 지정
-- 학생은 학과에 소속
-- 학생이름과 학과이름은 null 허용하지 않음
-- 학년은 4를 기본값으로 범위는 1~4 설정

/*
create table department(
	dptNo char(10) not null primary key,
	dptName varchar(15) not null,
	dptTel varchar(15)
	);

create table student(
	stdNo varchar(10) not null primary key,
	stdName varchar(15) not null,
	stdYear int default 4 check(stdYear>=1 and stdYear<=4),
	stdAddress varchar(40),
	stdBirth date, 
	dptNo char(10) not null,
	constraint FK_std_Department foreign key(dptNo) references department(dptNo)
	);
    
                                  
CREATE TABLE professor (
    proNo CHAR(10) NOT NULL PRIMARY KEY,
    proName VARCHAR(30) NOT NULL,
    proPhone CHAR(20),
    dptNo CHAR(10) NOT NULL,
    CONSTRAINT FK_pro_department FOREIGN KEY (dptNo) REFERENCES department (dptNo)
);

CREATE TABLE course (
	courseCode CHAR(10) NOT NULL PRIMARY KEY,
    courseName VARCHAR(30) NOT NULL,
    courseCredit INT DEFAULT 3 CHECK (courseCredit >= 1 and courseCredit <= 6),
    proNo CHAR(10) NOT NULL,
    CONSTRAINT FK_course_professor FOREIGN KEY (proNo) REFERENCES professor (proNo)
);


-- 주 키를 복합키 형식으로 지정
create table scores(
	stdNo char(10) not null, 
    courseCode char(10) not null,
    score int default 0 not null check(score >=0 and score <= 100),
    grade char(10) not null,
    constraint PK_scores_stdNo_courseCode primary key (stdNo, courseCode),
	constraint FK_scores_student foreign Key (stdNo) references student(stdNo),
    constraint FP_scored_course foreign Key (courseCode) references course(courseCode)
);

-- 자동으로 아이디나 값이 증가 : auto_increment
create table board(
	boardNo int auto_increment not null primary key,
	boardTitle varchar(30) not null,
    boardAuthor varchar(20) not null,
    boardContent varchar(100) not null
    );
    */
    
-- Alter : 데이터베이스, 테이블, 뷰 등의 정보 수정(변경)

-- alter table board auto_increment = 100;
-- set @@auto_increment_increment = 3;

#변수 선언, count라는 변수에 0을 선언
-- update를 이용해서 게시판 boardNo 값을 일괄적으로 변경
-- set @count = 0;
-- update board set boardNo = @count:=@count+1;

    