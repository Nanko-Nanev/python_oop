from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        result = ""
        for doc in self.documents:
            result += str(doc)
        return result

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        current_category = [cat for cat in self.categories if cat.id == category_id][0]
        if current_category:
            current_category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        current_topic = [topic for topic in self.topics if topic.id == topic_id][0]
        if current_topic:
            current_topic.topic = new_topic
            current_topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        current_document = [document for document in self.documents if document.id == document_id][0]
        if current_document:
            current_document.file_name = new_file_name

    def delete_category(self, category_id):
        current_category = [cat for cat in self.categories if cat.id == category_id][0]
        if current_category:
            self.categories.remove(current_category)

    def delete_topic(self, topic_id):
        current_topic = [topic for topic in self.topics if topic.id == topic_id][0]
        if current_topic:
            self.topics.remove(current_topic)

    def delete_document(self, document_id):
        current_cod = [doc for doc in self.documents if doc.id == document_id][0]
        if current_cod:
            self.documents.remove(current_cod)

    def get_document(self, document_id):
        return [document for document in self.documents if document.id == document_id][0]

