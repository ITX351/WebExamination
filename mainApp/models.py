# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Klass(models.Model):  # 班级表, 类名冲突
    year = models.IntegerField()  # 年份
    number = models.IntegerField()  # 班号

    class META:
        ordering = ['year', 'number']


class Student(models.Model):  # 学生表
    number = models.CharField(max_length = 100)  # 学号
    name = models.CharField(max_length = 100)  # 姓名
    klass = models.ForeignKey(Klass)  # 班级

    def __unicode__(self):
        return self.name

    class META:
        ordering = ['number']


class Problem(models.Model):  # 题库表
    description = models.TextField()  # 题面
    solution = models.IntegerField()  # 标准答案
    choice1 = models.CharField(max_length = 255)  # 选项
    choice2 = models.CharField(max_length = 255)
    choice3 = models.CharField(max_length = 255)
    choice4 = models.CharField(max_length = 255)
    choice5 = models.CharField(max_length = 255)
    public = models.IntegerField(default = 0)  # 0 不公开, 1 公开
    correctTime = models.IntegerField(default = 0)  # 正确解答次数
    tryTime = models.IntegerField(default = 0)  # 总解答次数
    createdAt = models.DateTimeField(auto_created = True)  # 创建时间
    creator = models.ForeignKey(User, related_name = 'problem_creator')  # 创建者
    changedAt = models.DateTimeField(auto_now = True)  # 最后一次编辑时间
    changer = models.ForeignKey(User, related_name = 'problem_changer')  # 最后一次编辑者

    def __unicode__(self):
        return self.description


class Examination(models.Model):  # 考试表
    name = models.CharField(max_length = 255)  # 考试名称
    startTime = models.DateTimeField()  # 考试开始时间
    endTime = models.DateTimeField()  # 考试结束时间
    createdAt = models.DateTimeField(auto_created = True)
    creator = models.ForeignKey(User, related_name = 'examination_creator')
    problems = models.ManyToManyField(Problem, through = 'ExaminationProblem')

    def __unicode__(self):
        return self.name

    class META:
        ordering = ['-startTime']


class ExaminationProblem(models.Model):  # 考试试题表
    examination = models.ForeignKey(Examination)  # 考试场次
    problem = models.ForeignKey(Problem)  # 题目
    score = models.IntegerField()  # 分值


class Answer(models.Model):  # 学生作答表
    examinationProblem = models.ForeignKey(ExaminationProblem)  # 试题
    student = models.ForeignKey(Student)  # 学生
    choice = models.IntegerField()  # 学生作答
    solution = models.IntegerField()  # 标准答案, 考虑到标准答案可能变动


class Grade(models.Model):  # 学生成绩表
    examination = models.ForeignKey(Examination)  # 考试场次
    student = models.ForeignKey(Student)  # 学生
    totalScore = models.IntegerField()  # 分数
