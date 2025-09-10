# 🚦 Smart Traffic Violation Detector – Workflow

### Phase 1: Data Collection
- Scrape/download traffic images & videos → data/raw/
- Clean & preprocess dataset → data/processed/

### Phase 2: Data Annotation
- Label with LabelImg/Roboflow → YOLO format (.txt)
- Structure into train/, val/, test/ + dataset.yaml

### Phase 3: Model Training
- Use YOLOv5/YOLOv8 pre-trained weights
- Fine-tune with custom dataset → save in models/fine_tuned/

### Phase 4: Model Evaluation
- Evaluate (mAP, precision, recall, F1-score)
- Build src/inference.py for new image/video detection

### Phase 5: Deployment
- Backend → Flask / FastAPI (deployment/api.py)
- Frontend → Streamlit / simple UI
- Dockerize → Deploy to Heroku / AWS / GCP

### Phase 6: Maintenance
- Version models (models/v1, v2)
- Expand dataset & improve accuracy over time

Directory ↔ Flow Mapping:
- data/ → Phases 1–2
- notebooks/ → Phase 4
- models/ → Phases 3–4
- src/ → Phases 4–5
- deployment/ → Phase 5
- utils/ → Helpers
