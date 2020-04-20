class Article:
    def __init__(self):
        self.num = 0    # 글번호
        self.title = 0  # 제목
        
class FileArticle(Article):
    def __init__(self):
        self.fileName = 0       # 파일 이름
    def __str__(self):
        return '자료실 [번호={}, 제목={}, 첨부파일={}]'.format(
            self.num, self.title, self.fileName)
    
class QNArticle(Article):
    def __init__(self):
        self.answer = 0       # 답변 
    def __str__(self):
        return '질문/답변 [글번호={}, 제목={}, 답변={}]'.format(
            self.num, self.title, self.answer)
    
fileArticle = FileArticle()
fileArticle.num = 1
fileArticle.title = '첫번째 자료입니다. '
fileArticle.fileName = 'python.ppt'
print(fileArticle)
print('-'*40)

qnaArticle = QNArticle()
qnaArticle.num = 1
qnaArticle.title = '첫번째 질문입니다. '
qnaArticle.answer = '첫번째 답변입니다.'
print(qnaArticle)
print('-'*40)

'''
자료실 [번호=1, 제목=첫번째 자료입니다. , 첨부파일=python.ppt]
----------------------------------------
질문/답변 [글번호=1, 제목=첫번째 질문입니다. , 답변=첫번째 답변입니다.]
'''