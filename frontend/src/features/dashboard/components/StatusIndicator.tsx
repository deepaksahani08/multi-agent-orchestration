"use client";

import { motion } from "motion/react";
import {
  AlertCircle,
  CheckCircle2,
  LoaderCircle,
} from "lucide-react";

type WorkflowStatus =
  | "pending"
  | "running"
  | "completed"
  | "failed";

type Props = {
  status: WorkflowStatus;
};

export function StatusIndicator({ status }: Props) {
  switch (status) {
    case "running":
      return (
        <motion.div
          initial={{ opacity: 0.8 }}
          animate={{
            opacity: [0.6, 1, 0.6],
          }}
          transition={{
            repeat: Infinity,
            duration: 1.2,
          }}
          className="flex items-center gap-2 text-primary"
        >
          <LoaderCircle className="size-4 animate-spin" />

          <span className="text-sm font-medium">
            Running...
          </span>
        </motion.div>
      );

    case "completed":
      return (
        <div className="flex items-center gap-2 text-green-600">
          <CheckCircle2 className="size-4" />

          <span className="text-sm font-medium">
            Completed
          </span>
        </div>
      );

    case "failed":
      return (
        <div className="flex items-center gap-2 text-red-600">
          <AlertCircle className="size-4" />

          <span className="text-sm font-medium">
            Failed
          </span>
        </div>
      );

    default:
      return (
        <div className="flex items-center gap-2 text-muted-foreground">
          <div className="size-2 rounded-full bg-muted-foreground" />

          <span className="text-sm">
            Pending
          </span>
        </div>
      );
  }
}