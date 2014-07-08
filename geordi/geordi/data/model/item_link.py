from . import db


class ItemLink(db.Model):
    __tablename__ = 'item_link'
    __table_args__ = {'schema': 'geordi'}

    type = db.Column(db.Unicode, nullable=False, primary_key=True)
    item_id = db.Column('item', db.Integer, db.ForeignKey('geordi.item.id', ondelete='CASCADE'), primary_key=True)
    linked_id = db.Column('linked', db.Integer, db.ForeignKey('geordi.item.id', ondelete='CASCADE'), primary_key=True)

    def to_dict(self):
        response = dict(type=self.type,
                        item_id=self.item_id,
                        linked_id=self.linked_id)
        return response

    @classmethod
    def get(cls, type, item_id, linked_id, **kwargs):
        return cls.query.filter_by(type=type, item_id=item_id, linked_id=linked_id, **kwargs).first()

    @classmethod
    def get_by_item_id(cls, item_id, **kwargs):
        return cls.query.filter_by(item_id=item_id, **kwargs).all()

    def delete(self):
        db.session.delete(self)
        db.session.flush()
        return self

    @classmethod
    def find_or_insert(cls, node_item, target_item, link_type):
        link = cls.get(type=link_type, item_id=node_item, linked_id=target_item)
        if link is None:
            link = db.session.add(cls(type=link_type, item_id=node_item, linked_id=target_item))
            db.session.flush()
        return link

    @classmethod
    def delete_by_item_id(cls, item_id, **kwargs):
        cls.query.filter_by(item_id=item_id, **kwargs).delete()
        db.session.flush()