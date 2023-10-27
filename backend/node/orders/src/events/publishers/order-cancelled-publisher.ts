import { Subjects, Publisher, OrderCancelledEvent } from '@scriptmotor/common';

export class OrderCancelledPublisher extends Publisher<OrderCancelledEvent> {
  subject: Subjects.OrderCancelled = Subjects.OrderCancelled;
}
