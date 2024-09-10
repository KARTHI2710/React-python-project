import "./Model.css"

const Model = () => {
  return (
    <div className="modalcontainer">
      <div className="modal">
          <div className="heading">
            <h3>Add Friend</h3>
            <span>&times;</span>
          </div>
          <div className="name-age">
            <div className="form-control">
              <label htmlFor="name" className="form-label">
                Full Name
                <input type="text" id="name" className="form-text" />
              </label>
            </div>
            <div className="form-control">
              <label htmlFor="name" className="form-label">
                Role
                <input type="text" id="name" className="form-text" />
              </label>
            </div>
          </div>

          <div className="description">
            <label htmlFor="desc">
              Description
              <textarea name="descrition" id="desc" className="form-desc"></textarea>
            </label>
          </div>
          <div className="gender">
            <label>
              <input
                type="radio"
                value="male"
              />
              Male
            </label>
  
            <label>
              <input
                type="radio"
                value="female"
              />
              Female
            </label>

          </div>

          <div className="buttons">
            <button className="add">Add</button>
            <button className="cancel">cancel</button>
          </div>

      </div>
      
      
    </div>
  )
}

export default Model
