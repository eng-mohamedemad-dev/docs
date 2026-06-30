# Chapter Two Image Requirements

Do not insert these images into the generated document automatically. Replace each
matching placeholder manually in Microsoft Word.

## General specifications

- Use high-resolution images with no watermarks.
- Diagrams should use a white background and the CrimeLens cyan, navy, and gold accents.
- Landscape diagrams: 16:9, minimum width 1920 px.
- Chapter background: vertical A4 or 4:5 crop, minimum 2480 × 3000 px.
- Use English labels only.
- Preserve the exact filename shown below.

## Required images

1. `CH02_Literature_Review_Background.jpg`
   - A modern research-oriented collage combining surveillance cameras, video frames,
     neural-network connections, and academic-paper motifs.
   - Avoid readable company logos or copyrighted interface screenshots.

2. `CH02_FIG_02_Method_Evolution_Timeline.png`
   - Timeline: handcrafted motion features → 2D CNN → two-stream networks → 3D CNN /
     recurrent models → autoencoder and prediction → MIL → attention and transformers.

3. `CH02_FIG_03_Anomaly_Context_Taxonomy.png`
   - Taxonomy separating point, contextual, collective, and object-level anomalies,
     with one simple surveillance example for each category.

4. `CH02_FIG_04_Supervision_Paradigms.png`
   - Continuum comparing fully supervised, semi-supervised/one-class, weakly supervised,
     and self-supervised learning by annotation cost and localization precision.

5. `CH02_FIG_05_Feature_Representations.png`
   - One video input branching into RGB appearance, optical flow, spatiotemporal volume,
     object tracks/relations, scene context, and audio features.

6. `CH02_FIG_06_Literature_Review_Workflow.png`
   - Flowchart: supplied survey → primary-paper selection → task/dataset/metric extraction
     → comparability check → synthesis → research gaps.

7. `CH02_FIG_07_Algorithm_Taxonomy.png`
   - Hierarchical map of discriminative, reconstruction, prediction, weak-supervision,
     object-detection, recurrent, transformer, and multimodal methods.

8. `CH02_FIG_08_2D_CNN_Pipeline.png`
   - Frame sampling → resizing/normalization → convolutional backbone → pooling →
     classifier → temporal score smoothing.

9. `CH02_FIG_09_Two_Stream_Optical_Flow.png`
   - Parallel RGB spatial stream and optical-flow temporal stream followed by score or
     feature fusion.

10. `CH02_FIG_10_3D_CNN_Video_Volume.png`
    - A stack of consecutive frames with a 3 × 3 × 3 kernel illustrating convolution
      over width, height, and time.

11. `CH02_FIG_11_Recurrent_Temporal_Model.png`
    - CNN features extracted from consecutive frames and passed through LSTM/ConvLSTM
      cells to produce temporal event probabilities.

12. `CH02_FIG_12_Autoencoder_Anomaly_Scoring.png`
    - Normal frame/clip → encoder → latent representation → decoder → reconstruction →
      reconstruction-error anomaly score.

13. `CH02_FIG_13_Future_Frame_Prediction.png`
    - Previous frames → prediction network → predicted future frame compared with the
      real future frame → prediction-error score.

14. `CH02_FIG_14_GAN_Anomaly_Framework.png`
    - Generator and discriminator interaction for normal-video reconstruction or future
      prediction, with the resulting anomaly score.

15. `CH02_FIG_15_MIL_Bags_Instances.png`
    - Normal and abnormal videos represented as bags, divided into temporal instances,
      with the highest abnormal segment score highlighted.

16. `CH02_FIG_16_RTFM_Feature_Magnitude.png`
    - Temporal segments, feature magnitudes, hard-instance selection, dilated temporal
      convolution, and self-attention.

17. `CH02_FIG_17_YOLO_Object_Evidence.png`
    - Surveillance frame → YOLO detector → weapon/fire/person boxes → tracking or scene
      context → event evidence.

18. `CH02_FIG_18_Video_Transformer_Attention.png`
    - Video divided into frame patches/tokens, followed by separate spatial and temporal
      attention blocks.

19. `CH02_FIG_19_Audio_Visual_Fusion.png`
    - Video branch and audio branch with synchronized features and an audio-visual
      violence score.

20. `CH02_FIG_20_Hybrid_Evidence_Fusion.png`
    - Object detection, action classification, anomaly score, audio, and scene metadata
      combined through feature-, score-, and decision-level fusion.

21. `CH02_FIG_21_Metrics_Thresholds.png`
    - Confusion matrix plus ROC and Precision–Recall curves showing how threshold changes
      precision, recall, and false alarms.

22. `CH02_FIG_22_Dataset_Landscape.png`
    - Bubble or matrix chart positioning UCSD, Avenue, ShanghaiTech, UCF-Crime,
      RWF-2000, and XD-Violence by duration, realism, annotation level, and modality.

23. `CH02_FIG_23_UCF_Crime_Categories.png`
    - Thirteen UCF-Crime anomaly categories grouped visually, with normal and anomalous
      videos illustrated as weakly labeled long timelines.

24. `CH02_FIG_24_Compact_Benchmark_Scenes.jpg`
    - A labeled montage containing representative UCSD Ped1/Ped2, CUHK Avenue, and
      ShanghaiTech scenes. Use only legally reusable dataset samples.

25. `CH02_FIG_25_Violence_Datasets.png`
    - Side-by-side comparison of RWF-2000 and XD-Violence: size, clip type, modality,
      labels, and primary task.

26. `CH02_FIG_26_Domain_Shift.png`
    - The same event represented under different cameras, lighting, weather, resolution,
      viewpoint, crowd density, and compression conditions.

27. `CH02_FIG_27_Literature_Timeline.png`
    - Chronological timeline of representative methods and datasets from autoencoder
      regularity learning and C3D through UCF-Crime, future-frame prediction, RWF-2000,
      XD-Violence, RTFM, TimeSformer, ViViT, and the 2025 survey.

28. `CH02_FIG_28_Research_Gap_Map.png`
    - Research gaps mapped to opportunities: context dependence, label scarcity,
      false alarms, domain shift, explainability, privacy, compute, and multimodal
      synchronization.
