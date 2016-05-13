from conductor.tests import TestCase


class TestSupportTicket(TestCase):

    def test_factory(self):
        ticket = self.SupportTicketFactory.build()
        self.assertGreater(len(ticket.subject), 0)
        self.assertGreater(len(ticket.message), 0)

    def test_str(self):
        ticket = self.SupportTicketFactory.build(subject='Halp!')
        self.assertEqual('Halp!', str(ticket))

    def test_has_subject(self):
        ticket = self.SupportTicketFactory.build(subject='Halp!')
        self.assertEqual('Halp!', ticket.subject)

    def test_has_message(self):
        ticket = self.SupportTicketFactory.build(message='How do you internet?')
        self.assertEqual('How do you internet?', ticket.message)
