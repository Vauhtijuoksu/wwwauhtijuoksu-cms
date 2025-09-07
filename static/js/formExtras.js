const Constraint = {
  FREE: "O",
  NO: "X",
  MAYBE: "?",
}
const multiplier = [
  [5,7,8,9,9,9,8,7,6,5,5,5,4,4,4,3,3,2,2,2,2,3,4,5], //monday-thursday
  [5,7,8,9,9,9,8,7,6,5,5,5,4,4,3,3,2,2,1,1,1,1,1,2], //friday
  [3,4,6,7,8,8,7,6,5,4,3,2,1,1,1,1,1,1,1,1,1,1,1,2], //saturday
  [3,4,6,7,8,8,7,6,5,4,3,2,1,2,2,2,2,3,3,3,3,3,3,3], //sunday
]
class TimeConstraintWidget {
  constraints  = []
  dayFlipValues = []
  hourFlipValues = []
  fieldName

  constructor(days, fieldName) {
    this.fieldName = fieldName
    for (let d = 0; d < days; d++){
      const day = []
      for (let h = 0; h < 24; h++){
        day.push(Constraint.FREE)
        if(d === 0){
          this.hourFlipValues.push(Constraint.FREE)
        }
      }
      this.dayFlipValues.push(Constraint.FREE)
      this.constraints.push(day)
    }
    this.getDataFromElement()
  }
  setNextValue(day, hour) {
    if (typeof day != 'undefined' && typeof hour != 'undefined'){
      const next = this.nextValue(this.constraints[day][hour])
      this.constraints[day][hour] = next
      this.setButtonStyle("tc-input-" + this.fieldName + "-" + day + "-" + hour,  next)
    } else if (typeof day != 'undefined') {
      const next = this.nextValue(this.dayFlipValues[day])
      this.dayFlipValues[day] = next
      this.setButtonStyle('tc-day-input-' + this.fieldName + "-" + day,  this.nextValue(next))
      for (let h = 0; h < this.hourFlipValues.length; h++){
        this.constraints[day][h] = next
        this.setButtonStyle("tc-input-" + this.fieldName + "-" + day + "-" + h,  next)
      }
    } else if (typeof hour != 'undefined') {
      const next = this.nextValue(this.hourFlipValues[hour])
      this.hourFlipValues[hour] = next
      this.setButtonStyle('tc-hour-input-' + this.fieldName + "-" + hour,  this.nextValue(next))
      for (let d = 0; d < this.dayFlipValues.length; d++){
        this.constraints[d][hour] = next
        this.setButtonStyle("tc-input-" + this.fieldName + "-" + d + "-" + hour,  next)
      }
    }
    this.updateInputElement()
    this.calculateScore()
  }
  updateInputElement() {
    const element = document.getElementById('id_'+this.fieldName)
    if (!element) return
    element.value = this.constraints.map((d) => {
      return d.join('')
    }).join("-")
  }
  getDataFromElement() {
    const element = document.getElementById('id_'+this.fieldName)
    if (!element) return
    const data = element.value
    const conArray = [Constraint.FREE, Constraint.NO, Constraint.MAYBE]
    if (data !== ''){
      data.split("-").forEach((hs, d) => {
        hs.split('').forEach((c, h) => {
          if (conArray.indexOf(c) >= 0){
            this.constraints[d][h] = c
          } else {
            this.constraints[d][h] = Constraint.FREE
          }
        })
      })
    }
    this.updateButtonStyles()
  }
  nextValue(current, forwards = true) {
    if (!forwards) current = this.nextValue(current) // just goes twice.
    switch (current){
      case Constraint.FREE:
        return Constraint.NO
      case Constraint.NO:
        return Constraint.MAYBE
      case Constraint.MAYBE:
        return Constraint.FREE
      }
  }
  updateButtonStyles(){
    for (let d = 0; d < this.constraints.length; d ++){
      for (let h = 0; h < 24; h++){
        this.setButtonStyle("tc-input-" + this.fieldName + "-" + d + "-" + h,  this.constraints[d][h])
        if (d===0){
          this.setButtonStyle('tc-hour-input-' + this.fieldName + "-" + h, this.nextValue(this.hourFlipValues[h]))
        }
      }
      this.setButtonStyle('tc-day-input-' + this.fieldName + "-" + d, this.nextValue(this.hourFlipValues[d]))
    }
  }
  setButtonStyle(elementID, c) {
    const element = document.getElementById(elementID)
    if (!element) return
    element.classList.remove('ok')
    element.classList.remove('notok')
    element.classList.remove('maybe')
    switch (c) {
      case Constraint.FREE:
        element.classList.add('ok')
        return
      case Constraint.NO:
        element.classList.add('notok')
        return
      case Constraint.MAYBE:
        element.classList.add('maybe')
        return
    }
  }
  calculateScore() {
    let total = 0
    let weightedTotal = 0
    let score = 0
    let weightedScore = 0
    for (let d = 0; d < this.constraints.length; d++) {
      const dayMultiplier = multiplier[Math.max(0, 3 + d - (this.constraints.length - 1))]
      for (let h = 0; h < 24; h++) {
        if ((d > 0 || h >= 10) && (d < this.constraints.length - 1 || h >= 20)) {
          total += 1
          weightedTotal += dayMultiplier[h]
          switch (this.constraints[d][h]) {
            case Constraint.FREE:
              score += 1
              weightedScore += dayMultiplier[h]
              break
            case Constraint.NO:
              break
            case Constraint.MAYBE:
              score += 0.1
              weightedScore += 0.1 * dayMultiplier[h]
              break
          }
        }
      }
    }
    const scoreIndex = this.getScoreIndex(weightedScore/weightedTotal)
    const viuhtiScoreIndicators = document.getElementsByClassName('tc-score-indicator-' + this.fieldName)
    for (let e = 0; e < viuhtiScoreIndicators.length; e++){
      viuhtiScoreIndicators[e].classList.remove('active')
    }
    const element = document.getElementById('tc-score-indicator-' + this.fieldName + "-" + scoreIndex)
    if (element) element.classList.add('active')
  }

  getScoreIndex(score) {
    const thresholds = [0.8,0.65,0.5,0.4,0.3,0.18,0.06,0.02,0.01,-1]
    for (let s = 0; s < thresholds.length; s++){
      if (score > thresholds[s]) return s
    }
  }
}