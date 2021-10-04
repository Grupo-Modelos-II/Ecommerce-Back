from sqlalchemy.orm import Session

from dto.Category import CategoryRequest, CategoryResponse

from model import Category

def delete_category_service(session: Session, id) -> bool:
    category = session.query(Category).get(id)
    session.delete(category)
    session.commit()
    session.refresh(category)
    return category is None

def create_category_service(session: Session, request: CategoryRequest) -> CategoryResponse:
    category = Category(**request.dict())
    session.add(category)
    session.commit()
    return CategoryResponse(**category.to_dict())

def get_categories_service(session: Session) -> list[CategoryResponse]:
    categories = session.query(Category).all()
    return [CategoryResponse(**category.to_list()) for category in categories]

def get_category_service(session: Session, id) -> CategoryResponse:
    category = session.query(Category).get(id)
    return CategoryResponse(**category.to_list()) if category else None