from ..utils import make_psuedo_id
from .base import BaseModel, cleanup_list, SourceMixin
from .bill import Bill
from .popolo import Organization
from .schemas.vote import schema


class Vote(BaseModel, SourceMixin):
    _type = 'vote'
    _schema = schema

    def __init__(self, session, motion, start_date, classification, outcome,
                 identifier='', bill=None, organization=None, chamber=None, **kwargs):
        super(Vote, self).__init__()

        self.session = session
        self.motion = motion
        self.start_date = start_date
        self.classification = cleanup_list(classification, [])
        self.outcome = outcome
        self.identifier = identifier
        self.organization = organization

        self.set_bill(bill)
        self.votes = []
        self.counts = []

        if organization and chamber:
            raise ValueError('cannot specify both chamber and organization')
        elif chamber:
            self.organization = make_psuedo_id(classification='legislature', chamber=chamber)
        elif organization:
            if isinstance(organization, Organization):
                self.organization = organization._id
            else:
                self.organization = make_psuedo_id(**organization)
        else:
            # neither specified
            self.organization = make_psuedo_id(classification='legislature')

    def __str__(self):
        return u'{0} - {1} - {2}'.format(self.session, self.start_date, self.motion)

    __unicode__ = __str__

    def set_bill(self, bill_or_name, chamber=None):
        if not bill_or_name:
            self.bill = None
        elif isinstance(bill_or_name, Bill):
            if chamber:
                raise ValueError("set_bill takes no arguments when using a `Bill` object")
            self.bill = bill_or_name._id
        else:
            kwargs = {'name': bill_or_name, 'from_organization__classification': 'legislature'}
            if chamber:
                kwargs['from_organization__chamber'] = chamber
            self.bill = make_psuedo_id(**kwargs)

    def vote(self, option, voter):
        self.votes.append({"option": option, "voter_name": voter})

    def yes(self, name, id=None):
        return self.vote('yes', name)

    def no(self, name, id=None):
        return self.vote('no', name)

    def set_count(self, option, value):
        for co in self.counts:
            if co['option'] == option:
                co['value'] = value
                break
        else:
            self.counts.append({'option': option, 'value': value})