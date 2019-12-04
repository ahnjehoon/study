﻿namespace RestAPIServer.Models
{
    public class SensorRawData
    {
        public string SensorCode { get; set; }
        public long ValueOccurTime { get; set; }
        public long ValueSaveTime { get; set; }
        public string Value { get; set; }

        public void CopyData(SensorRawData param)
        {
            this.SensorCode = param.SensorCode;
            this.ValueOccurTime = param.ValueOccurTime;
            this.ValueSaveTime = param.ValueSaveTime;
            this.Value = param.Value;
        }
    }
}
