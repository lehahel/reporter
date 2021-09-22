import typing
import pdflatex


from pylatex import Document, Section, Subsection, Command, Itemize, Enumerate
from pylatex.utils import italic, NoEscape


class _Ticket:
    def __init__(self, name: str):
        self.reference = f"https://st.yandex-team.ru/{name.strip()}"

    def __str__(self):
        return self.reference

    def __eq__(self, other):
        return self.reference == other.reference


class _TicketGroup:
    def __init__(self, tickets: typing.List[_Ticket] = None, description: str = None):
        self.tickets: typing.List[_Ticket] = tickets if tickets is not None else []
        self.description: str = description.strip()

    def add_ticket(self, ticket: str):
        self.tickets.append(_Ticket(ticket))

    def remove_ticket(self, ticket: str):
        self.tickets.remove(_Ticket(ticket))

    def __str__(self):
        result: str = self.description
        result += ':\n' if len(self.tickets) > 0 else '\n'
        for ticket in self.tickets:
            result += '  - ' + str(ticket) + '\n'
        return result

    def append_to_tex(self, doc: Document):
        with doc.create(Subsection(self.description)):
            with doc.create(Itemize()) as ticket_list:
                for ticket in self.tickets:
                    ticket_list.add_item(str(ticket))

    def __eq__(self, other):
        return set(self.tickets) == set(other.tickets)


class Report:
    def __init__(self, name: str = ''):
        self.name = name.strip()
        self.points: typing.List[_TicketGroup] = []

    def change_name(self, name):
        self.name = name.strip()

    def add_ticket(self, point: int, ticket: str):
        if 1 <= point <= len(self.points):
            self.points[point - 1].add_ticket(ticket)

    def remove_ticket(self, point: int, ticket: str):
        if 1 <= point <= len(self.points):
            self.points[point - 1].remove_ticket(ticket)

    def add_point(self, description: str = None):
        self.points.append(_TicketGroup(description=description))

    def remove_point(self, point: int):
        del self.points[point]

    def __str__(self):
        result = self.name + '\n' if self.name != '' else ''
        for (idx, point) in enumerate(self.points):
            result += str(idx + 1) + '. ' + str(point) + '\n'
        return result

    def export_as_pdf(self):
        doc = Document()
        with doc.create(Section(self.name)):
            with doc.create(Enumerate()) as enum:
                for point in self.points:
                    enum.add_item(str(point))
        doc.generate_pdf(self.name, clean_tex=False, compiler='pdflatex')
