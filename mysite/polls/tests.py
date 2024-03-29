from asyncio import futures
from django.test import TestCase

import datetime
from django.utils import timezone
from .models import Question

# Create your tests here.
class QuestionMethodTests(TestCase):
	def test_was_publishec_recently_with_future_question(self):
		"""test_was_publishec_recently_with_future_question 在将来发布的问卷应该返回False
		"""		
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), False)