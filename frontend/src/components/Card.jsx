
import "./Card.css"


const Card = (props) => {

  return (
    <div className="cardcontainer">
        <div className="card-header">
            <div className="icon">
            <img src={props.user.imgUrl} />
            </div>
            <div className="info">
                <h3 className="name">{props.user.name}</h3>
                <p className="designation">
                    {props.user.designation}
                </p>
            </div>
            <div className="buttons">
                <a href="#"><img src="edit.svg"/></a>
                <a href="#"><img src="delete.svg"/></a>
            </div>
        </div>
        <div className="desctiption">
            <p>{props.user.description}</p>
        </div>      
    </div>
    
  )
}

export default Card
