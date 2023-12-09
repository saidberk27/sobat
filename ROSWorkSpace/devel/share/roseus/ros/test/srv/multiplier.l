;; Auto-generated. Do not edit!


(when (boundp 'test::multiplier)
  (if (not (find-package "TEST"))
    (make-package "TEST"))
  (shadow 'multiplier (find-package "TEST")))
(unless (find-package "TEST::MULTIPLIER")
  (make-package "TEST::MULTIPLIER"))
(unless (find-package "TEST::MULTIPLIERREQUEST")
  (make-package "TEST::MULTIPLIERREQUEST"))
(unless (find-package "TEST::MULTIPLIERRESPONSE")
  (make-package "TEST::MULTIPLIERRESPONSE"))

(in-package "ROS")





(defclass test::multiplierRequest
  :super ros::object
  :slots (_a _b ))

(defmethod test::multiplierRequest
  (:init
   (&key
    ((:a __a) 0)
    ((:b __b) 0)
    )
   (send-super :init)
   (setq _a (round __a))
   (setq _b (round __b))
   self)
  (:a
   (&optional __a)
   (if __a (setq _a __a)) _a)
  (:b
   (&optional __b)
   (if __b (setq _b __b)) _b)
  (:serialization-length
   ()
   (+
    ;; int32 _a
    4
    ;; int32 _b
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _a
       (write-long _a s)
     ;; int32 _b
       (write-long _b s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _a
     (setq _a (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _b
     (setq _b (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass test::multiplierResponse
  :super ros::object
  :slots (_result ))

(defmethod test::multiplierResponse
  (:init
   (&key
    ((:result __result) 0)
    )
   (send-super :init)
   (setq _result (round __result))
   self)
  (:result
   (&optional __result)
   (if __result (setq _result __result)) _result)
  (:serialization-length
   ()
   (+
    ;; int32 _result
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _result
       (write-long _result s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _result
     (setq _result (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass test::multiplier
  :super ros::object
  :slots ())

(setf (get test::multiplier :md5sum-) "a7d7d7065d45755acef7d4dcf908162a")
(setf (get test::multiplier :datatype-) "test/multiplier")
(setf (get test::multiplier :request) test::multiplierRequest)
(setf (get test::multiplier :response) test::multiplierResponse)

(defmethod test::multiplierRequest
  (:response () (instance test::multiplierResponse :init)))

(setf (get test::multiplierRequest :md5sum-) "a7d7d7065d45755acef7d4dcf908162a")
(setf (get test::multiplierRequest :datatype-) "test/multiplierRequest")
(setf (get test::multiplierRequest :definition-)
      "int32 a
int32 b
---
int32 result
")

(setf (get test::multiplierResponse :md5sum-) "a7d7d7065d45755acef7d4dcf908162a")
(setf (get test::multiplierResponse :datatype-) "test/multiplierResponse")
(setf (get test::multiplierResponse :definition-)
      "int32 a
int32 b
---
int32 result
")



(provide :test/multiplier "a7d7d7065d45755acef7d4dcf908162a")


